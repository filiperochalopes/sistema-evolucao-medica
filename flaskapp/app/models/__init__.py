
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
import enum
import bcrypt


class SexEnum(enum.Enum):
    male = 'Masculino'
    fema = 'Feminino'


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), unique=True, nullable=False)

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password, bcrypt.gensalt())

    def verify_password(self, password):
        return bcrypt.checkpw(password, self.password_hash)


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sex = db.Column(db.Enum(SexEnum), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    admission_date = db.Column(db.Date, nullable=False)
    admission_hour = db.Column(db.Time)
    hpi = db.Column(
        db.Text, comment="History of the Present Illness / HMA", nullable=False)
    waiting_vacancy = db.Column(
        db.Boolean, default=False, comment="Aguardando vaga na Regulação")
    regulation_code = db.Column(
        db.String, comment="Número de registro da regulação")
    pendings = db.Column(db.Text, nullable=False)

    evolutions = relationship('Evolution')
    # timestamps
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # Se removido deve ir para outra lista, lista das "Altas ou Transferências"
    removed_at = db.Column(db.DateTime(timezone=True))


class Evolution(db.Model):
    __tablename__ = 'evolutions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(
        db.Text, comment="Evolução do paciente com exame físico e sinais vitais")

    patient_id = db.Column(db.Integer, ForeignKey('patients.id'))

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
