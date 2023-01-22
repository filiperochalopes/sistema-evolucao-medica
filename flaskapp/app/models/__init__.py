import enum
import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table
from sqlalchemy.ext.hybrid import hybrid_property

from app.utils import calculate_age


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
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, unique=True)
    cns = db.Column(db.String, unique=True)
    birthdate = db.Column(db.Date, nullable=False)
    professional_category = db.Column(db.Enum(ProfessionalCategoryEnum), nullable=False)
    phone = db.Column(db.String)
    professional_document_uf = db.Column(db.String)
    professional_document_number = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)
    
    # timestamps
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @property
    def password(self):
        raise AttributeError('Senha não é um atributo capaz de ser lido')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password, bcrypt.gensalt()).decode()
    
    @staticmethod
    def generate_password(password:str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

    def verify_password(self, password):
        return bcrypt.checkpw(password, self.password_hash)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return not(self.is_annonymous())

    def is_annonymous(self):
        return not(self.is_authenticated())


class Config(db.Model):
    '''
    Model para configurações de ambiente, principalmente para cadastro de
    informações referentes à unidade central do sistema, no caso o Hospital
    Maternidade como nome completo, CNES, endereço e afins. Adicionar no seed
    '''

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String)
    value = db.Column(db.Text)


class Cid10(db.Model):
    __tablename__ = 'cid10'

    code = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String, nullable=False)
    complement = db.Column(db.String)
    number = db.Column(db.String)
    zip_code = db.Column(db.String, nullable=False)
    neighborhood = db.Column(db.String)
    uf = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)

"""
Models que vão ser populados por meio de registro de inputs médicos prévios
ExternalDrug, Comorbidity, Allergy, NursingActivity, RestingActivity
"""
class ExternalDrug(db.Model):
    '''Medicações prescritas para pacientes na hora da alta, prescrição externa, salvar para resuso'''

    __tablename__ = 'auto_external_drugs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    dosage = db.Column(db.String)

class Comorbidity(db.Model):
    __tablename__ = 'auto_comorbidities'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String, unique=True)


class Allergy(db.Model):
    __tablename__ = 'auto_allergies'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String, unique=True)


PatientComorbidity  = Table('_patient_comorbidity', 
    db.Model.metadata,
    db.Column('patient_id', db.Integer, ForeignKey('patients.id'), primary_key=True),
    db.Column('comorbidity_id', db.Integer, ForeignKey('auto_comorbidities.id'), primary_key=True))

PatientAllergy  = Table('_patient_allergy',
    db.Model.metadata,
    db.Column('patient_id', db.Integer, ForeignKey('patients.id'), primary_key=True),
    db.Column('allergy_id', db.Integer, ForeignKey('auto_allergies.id'), primary_key=True))

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    mother_name = db.Column(db.String, nullable=True)
    sex = db.Column(db.Enum(SexEnum), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String, unique=True)
    cns = db.Column(db.String, unique=True)
    rg = db.Column(db.String, unique=True)
    weight_kg = db.Column(db.Float)
    comorbidities = relationship('Comorbidity', secondary=PatientComorbidity)
    allergies = relationship('Allergy', secondary=PatientAllergy)
    address_id = db.Column(db.Integer, ForeignKey("address.id"))
    address = relationship('Address')

    # timestamps
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @hybrid_property
    def age(self):
        return calculate_age(self.birthdate)


DrugDrugGroupPreset = Table('_drug_group_preset',
    db.Model.metadata,
    db.Column('drug_group_preset_id', db.Integer, ForeignKey('drug_group_presets.id'), primary_key=True),
    db.Column('drug_id', db.Integer, ForeignKey('drugs.id'), primary_key=True))


class Drug(db.Model):
    __tablename__ = 'drugs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    usual_dosage = db.Column(db.String)
    usual_route = db.Column(db.String)
    comment = db.Column(
        db.Text, comment="Aqui pode colocar alguma dica de uso em pediatria, ou melhor aplicação de antibioticoterapia, além de restrição de uso")
    kind = db.Column(db.Enum(DrugKindEnum), nullable=False)
    drug_group_presets = relationship('DrugGroupPreset', secondary=DrugDrugGroupPreset, back_populates='drugs')


class DrugPrescription(db.Model):
    __tablename__ = 'drug_prescriptions'

    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, ForeignKey("drugs.id"))
    drug = relationship('Drug')
    dosage = db.Column(db.String)
    route = db.Column(db.String)
    initial_date = db.Column(db.DateTime)
    ending_date = db.Column(db.DateTime)

    prescription_id = db.Column(db.Integer, ForeignKey("prescriptions.id"))


class Diet(db.Model):
    __tablename__ = 'diets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class State(db.Model):
    __tablename__ = 'states'

    ibge_code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    uf = db.Column(db.String)


class RestingActivity(db.Model):
    # Determinar qual o grau de atividade/repouso do paciente
    __tablename__ = 'auto_resting_activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    prescriptions = relationship('Prescription', back_populates='resting_activity')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


NursingActivityPrescription = Table('_nursing_activity_prescription',
    db.Model.metadata,
    db.Column('nursing_activity_id', db.Integer, ForeignKey('auto_nursing_activities.id'), primary_key=True),
    db.Column('prescription_id', db.Integer, ForeignKey('prescriptions.id'), primary_key=True),
    db.Column('created_at', db.DateTime(timezone=True), server_default=func.now()))


class NursingActivity(db.Model):
    # Atividades de enfermagem como aferição de sinais vitais, checagem de FCF...
    __tablename__ = 'auto_nursing_activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # Caso alguém crie alguma atividade inadequada ou errada
    disabled = db.Column(db.Boolean, default=False)
    prescriptions = relationship('Prescription', secondary=NursingActivityPrescription, back_populates='nursing_activities')


class Internment(db.Model):
    __tablename__ = 'internments'

    id = db.Column(db.Integer, primary_key=True)
    admission_datetime = db.Column(db.DateTime, nullable=False)
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

    professional_id = db.Column(db.Integer, ForeignKey("users.id"))
    professional = relationship('User', foreign_keys=professional_id)

    cid10_code = db.Column(db.String, ForeignKey("cid10.code"))
    cid10 = relationship('Cid10')

    measures = relationship('Measure', back_populates='internment')
    fluid_balance = relationship('FluidBalance', back_populates='internment')
    evolutions = relationship('Evolution', back_populates='internment')
    prescriptions = relationship('Prescription', back_populates='internment')
    pendings = relationship('Pending', back_populates='internment')

    # timestamps
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    # Algumas colunas podem ser editadas como aguardando vaga, código da regulação e alta
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # Se removido deve ir para outra lista, lista das "Altas ou Transferências"
    finished_at = db.Column(db.DateTime(timezone=True))
    finished_by_id = db.Column(db.Integer, ForeignKey("users.id"))
    finished_by = relationship('User', foreign_keys=finished_by_id)


class Prescription(db.Model):
    __tablename__ = 'prescriptions'

    id = db.Column(db.Integer, primary_key=True)

    # Só temos uma atividade de repouso por prescrição
    resting_activity_id = db.Column(db.Integer, ForeignKey("auto_resting_activities.id"))
    resting_activity = relationship('RestingActivity', back_populates='prescriptions')
    # Só temos uma dieta por prescrição
    diet_id = db.Column(db.Integer, ForeignKey("diets.id"))
    diet = relationship('Diet')
    # Só podemos ter várias prescrições de medicamentos que são criadas especialmente para cada prescrição
    drug_prescriptions = relationship('DrugPrescription')
    # Só temos uma dieta por prescrição
    nursing_activities = relationship('NursingActivity', secondary=NursingActivityPrescription, back_populates='prescriptions')

    professional_id = db.Column(db.Integer, ForeignKey("users.id"))
    professional = relationship('User')

    internment_id = db.Column(db.Integer, ForeignKey('internments.id'))
    internment = relationship('Internment', back_populates='prescriptions')

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class DrugGroupPreset(db.Model):
    __tablename__ = 'drug_group_presets'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    name = db.Column(db.String)
    drugs = relationship('Drug', secondary=DrugDrugGroupPreset, back_populates='drug_group_presets')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Measure(db.Model):
    __tablename__ = 'measures'

    id = db.Column(db.Integer, primary_key=True)
    spO2 = db.Column(db.Integer)
    pain = db.Column(db.Integer)
    systolic_bp = db.Column(db.Integer)
    diastolic_bp = db.Column(db.Integer)
    cardiac_freq = db.Column(db.Integer)
    respiratory_freq = db.Column(db.Integer)
    celcius_axillary_temperature = db.Column(db.Integer)
    glucose = db.Column(db.Integer)
    fetal_cardiac_freq = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    professional_id = db.Column(db.Integer, ForeignKey("users.id"))
    professional = relationship('User')

    internment_id = db.Column(db.Integer, ForeignKey('internments.id'))
    internment = relationship('Internment', back_populates='measures')

    @validates('spO2')
    def validate_spO2(self, _, value):
        if value <= 0:
            raise ValueError("SpO2 deve ser maior que 0")
        if value >= 100:
            raise ValueError("Valor não natural de SpO2, deve ser menor que 100")
        return value

    @validates('systolic_bp')
    def validate_systolic_bp(self, _, value):
        if value is not None and self.diastolic_bp is None:
            raise ValueError("Pressão arterial diastólica deve ser preenchida")
        return value

class FluidBalanceDescription(db.Model):
    __tablename__ = 'fluid_balance_description'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)


class FluidBalance(db.Model):
    __tablename__ = 'fluid_balance'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    description_id = db.Column(db.Integer, ForeignKey('fluid_balance_description.id'))
    description = relationship('FluidBalanceDescription')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    professional_id = db.Column(db.Integer, ForeignKey("users.id"))
    professional = relationship('User')

    internment_id = db.Column(db.Integer, ForeignKey('internments.id'))
    internment = relationship('Internment', back_populates='fluid_balance')


class Evolution(db.Model):
    __tablename__ = 'evolutions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(
        db.Text, comment="Evolução do paciente com exame físico e sinais vitais")

    professional_id = db.Column(db.Integer, ForeignKey("users.id"))
    professional = relationship('User')

    internment_id = db.Column(db.Integer, ForeignKey('internments.id'))
    internment = relationship('Internment', back_populates='evolutions')

    cid10_code = db.Column(db.String, ForeignKey("cid10.code"))
    cid10 = relationship('Cid10')

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Pending(db.Model):
    __tablename__ = 'pendings'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(
        db.Text, comment="Evolução do paciente com exame físico e sinais vitais")
        
    professional_id = db.Column(db.Integer, ForeignKey("users.id"))
    professional = relationship('User')

    internment_id = db.Column(db.Integer, ForeignKey('internments.id'))
    internment = relationship('Internment', back_populates='pendings')

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class HighComplexityProcedure(db.Model):
    __tablename__ = 'high_complexity_procedures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    code = db.Column(db.String)