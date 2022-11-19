from datetime import datetime
import sys

from ariadne import convert_kwargs_to_snake_case

from app.graphql import mutation
from app.models import db, Internment, Measure
from app.utils.decorators import token_authorization

@mutation.field('createMeasure')
@convert_kwargs_to_snake_case
@token_authorization
def create_measure(_, info, internment_id:int, sp_o_2: int, pain: int, systolic_blood_pressure: int, diastolic_blood_pressure: int, cardiac_frequency: int, respiratory_frequency: int, celcius_axillary_temperature: int, glucose: int, fetal_cardiac_frequency: int, current_user: dict):
    # Determinando internamento
    internment = db.session.query(Internment).get(internment_id)
    # Determinando profissional que está registrando
    professional = current_user

    # Cria o registro de medições objetivas
    measure = Measure(spO2=sp_o_2, pain=pain, systolic_bp=systolic_blood_pressure, diastolic_bp=diastolic_blood_pressure, cardiac_freq=cardiac_frequency, respiratory_freq=respiratory_frequency, celcius_axillary_temperature=celcius_axillary_temperature, glucose=glucose, fetal_cardiac_freq=fetal_cardiac_frequency, professional_id=professional.id, internment_id=internment.id)
    db.session.add(measure)
    db.session.commit()
    
    return measure
