from app.graphql import query
from app.models import db, Patient, Allergy, Comorbidity
from app.serializers import PatientSchema
from ariadne import convert_kwargs_to_snake_case
from app.services.utils.auth import cpf_validator, cns_validator
from sqlalchemy import or_

@query.field("patient")
@convert_kwargs_to_snake_case
def patient(*_, id:int=None, query_name_cns_cpf:str=None):
    schema = PatientSchema()
    if id is not None:
        return schema.dump(db.session.query(Patient).get(id))
    if cpf_validator.validate(query_name_cns_cpf):
        # Caso seja um cpf válido, busca por cpf
        return schema.dump(db.session.query(Patient).filter(Patient.cpf == query_name_cns_cpf).one())
    if cns_validator.validate(query_name_cns_cpf):
        # Caso seja um cns válido, busca por cns
        return schema.dump(db.session.query(Patient).filter(Patient.cns == query_name_cns_cpf).one())
    return schema.dump(db.session.query(Patient).filter(Patient.name == query_name_cns_cpf).first())

@query.field("patients")
@convert_kwargs_to_snake_case
def patients(*_, query_name_cns_cpf:str=None, per_page:int=None, page:int=1):
    schema = PatientSchema(many=True)
    if query_name_cns_cpf is not None:
        if per_page is not None:
            return schema.dump(db.session.query(Patient).filter(or_(Patient.name.ilike(f'%{query_name_cns_cpf}%'), Patient.cns.ilike(f'%{query_name_cns_cpf}%'), Patient.cpf.ilike(f'%{query_name_cns_cpf}%'))))
        else:
            return schema.dump(db.session.query(Patient).filter(or_(Patient.name.ilike(f'%{query_name_cns_cpf}%'), Patient.cns.ilike(f'%{query_name_cns_cpf}%'), Patient.cpf.ilike(f'%{query_name_cns_cpf}%'))).paginate(page=page, per_page=per_page))
        
    return schema.dump(db.session.query(Patient).all())

@query.field("allergies")
def allergies(*_):
    return db.session.query(Allergy).all()

@query.field("comorbidities")
def comorbidities(*_):
    return db.session.query(Comorbidity).all()
