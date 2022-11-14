from app.graphql import query
from app.models import db, Patient, Allergy, Comorbidity
from app.serializers import PatientSchema

@query.field("patients")
def patient(*_, cns=None):
    if cns is not None:
        # Retorna o indivíduo único encontrado
        schema = PatientSchema()
        return schema.dump(db.session.query(Patient).filter(Patient.cns == cns).one())
    schema = PatientSchema(many=True)
    return schema.dump(db.session.query(Patient).all())

@query.field("allergies")
def allergies(*_):
    return db.session.query(Allergy).all()

@query.field("comorbidities")
def comorbidities(*_):
    return db.session.query(Comorbidity).all()