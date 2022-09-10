
from email.policy import default
from unicodedata import category
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
import enum
import bcrypt


class SexEnum(enum.Enum):
    male = 'Masculino'
    fema = 'Feminino'


class DrugKindEnum(enum.Enum):
    atb = 'Antibióticos'
    oth = 'Outros'


class ProfessionalCategoryEnum(enum.Enum):
    doc = 'Médico'
    nur = 'Enfermeira'
    tec = 'Técnica de Enfermagem'


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    @property
    def password(self):
        raise AttributeError('Senha não é um atributo capaz de ser lido')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password, bcrypt.gensalt())

    def verify_password(self, password):
        return bcrypt.checkpw(password, self.password_hash)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return not(self.is_annonymous())

    def is_annonymous(self):
        return not(self.is_authenticated())


class Professional(db.Model):
    __tablename__ = 'professionals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    cpf = db.Column(db.String)
    cns = db.Column(db.String)
    category = db.Column(db.Enum(ProfessionalCategoryEnum), nullable=False)
    number = db.Column(db.String)

    # timestamps
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class Cid10(db.Model):
    __tablename__ = 'cid10'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sex = db.Column(db.Enum(SexEnum), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    comorbidities = db.Column(db.Text)
    allergies = db.Column(db.Text)

    # timestamps
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class Drug(db.Model):
    __tablename__ = 'drugs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    usual_dosage = db.Column(db.String)
    comment = db.Column(
        db.Text, comment="Aqui pode colocar alguma dica de uso em pediatria, ou melhor aplicação de antibioticoterapia, além de restrição de uso")
    kind = db.Column(db.Enum(SexEnum), nullable=False)


class DrugPrescription(db.Model):
    __tablename__ = 'drug_prescriptions'

    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, ForeignKey("patients.id"))
    dosage = db.Column(db.String)
    initial_date = db.Column(db.Date)
    ending_date = db.Column(db.Date)


class Diet(db.Model):
    __tablename__ = 'diets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class RestingActivity(db.Model):
    # Determinar qual o grau de atividade/repouso do paciente
    __tablename__ = 'resting_activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class NursingActivity(db.Model):
    # Atividades de enfermagem como aferição de sinais vitais, checagem de FCF...
    __tablename__ = 'nursing_activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Internment(db.Model):
    __tablename__ = 'internments'

    id = db.Column(db.Integer, primary_key=True)
    admission_date = db.Column(db.Date, nullable=False)
    admission_hour = db.Column(db.Time)
    hpi = db.Column(
        db.Text, comment="History of the Present Illness / HMA", nullable=False)
    justification = db.Column(
        db.Text, comment="Justificativa de internamento", nullable=False)
    waiting_vacancy = db.Column(
        db.Boolean, default=False, comment="Aguardando vaga na Regulação")
    regulation_code = db.Column(
        db.String, comment="Número de registro da regulação")

    patient_id = db.Column(db.Integer, ForeignKey("patients.id"))
    patient = relationship('Patient')

    professional_id = db.Column(db.Integer, ForeignKey("professionals.id"))
    professional = relationship('Professional')

    cid10_code = db.Column(db.Integer, ForeignKey("cid10.code"))
    cid10 = relationship('Cid10')

    vitals = relationship('Vital')
    evolutions = relationship('Evolution')
    pendings = relationship('Pending')

    # timestamps
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    # Se removido deve ir para outra lista, lista das "Altas ou Transferências"
    removed_at = db.Column(db.DateTime(timezone=True))


class Prescription(db.Model):
    __tablename__ = 'prescriptions'

    id = db.Column(db.Integer, primary_key=True)
    diet_id = db.Column(db.Integer, ForeignKey("diets.id"))
    diet = relationship('Diet')
    resting_activities = relationship('RestingActivity')
    nursing_activities = relationship('NursingActivity')
    drug_prescriptions = relationship('DrugPrescription')


class Vital(db.Model):
    __tablename__ = 'vitals'

    id = db.Column(db.Integer, primary_key=True)
    spO2 = db.Column(db.Integer)
    pain = db.Column(db.Integer)
    sistolic_bp = db.Column(db.Integer)
    diastolic_bp = db.Column(db.Integer)
    cardiac_freq = db.Column(db.Integer)
    respiratory_freq = db.Column(db.Integer)
    celcius_axillary_temperature = db.Column(db.Integer)
    glucose = db.Column(db.Integer)

    @validates('spO2')
    def validate_email(self, _, value):
        assert value > 0
        assert value <= 100
        return value


class Evolution(db.Model):
    __tablename__ = 'evolutions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(
        db.Text, comment="Evolução do paciente com exame físico e sinais vitais")
    professional = db.Column(db.Integer, nullable=False)

    internment_id = db.Column(db.Integer, ForeignKey('internments.id'))
    internment = relationship('Internment')

    cid10_code = db.Column(db.Integer, ForeignKey("cid10.code"))
    cid10 = relationship('Cid10')

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())


class Pending(db.Model):
    __tablename__ = 'pendings'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(
        db.Text, comment="Evolução do paciente com exame físico e sinais vitais")
    professional = db.Column(db.Integer, nullable=False)

    internment_id = db.Column(db.Integer, ForeignKey('internments.id'))
    internment = relationship('Internment')

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
