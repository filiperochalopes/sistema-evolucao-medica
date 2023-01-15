from datetime import datetime
import sys

from ariadne import convert_kwargs_to_snake_case

from app.graphql import mutation
from app.models import db, Internment, Measure
from app.services.utils.decorators import token_authorization


@mutation.field('createMeasure')
@convert_kwargs_to_snake_case
@token_authorization
def create_measure(_, info, internment_id: int, sp_o_2: int = None, pain: int = None, systolic_blood_pressure: int = None, diastolic_blood_pressure: int = None, cardiac_frequency: int = None, respiratory_frequency: int = None, celcius_axillary_temperature: int = None, glucose: int = None, fetal_cardiac_frequency: int = None, current_user: dict = None):
    # Determinando internamento
    internment = db.session.query(Internment).get(internment_id)
    # Determinando profissional que está registrando
    professional = current_user

    # Cria o registro de medições objetivas
    measure = Measure(spO2=sp_o_2, pain=pain, diastolic_bp=diastolic_blood_pressure, systolic_bp=systolic_blood_pressure,  cardiac_freq=cardiac_frequency, respiratory_freq=respiratory_frequency,
                      celcius_axillary_temperature=celcius_axillary_temperature, glucose=glucose, fetal_cardiac_freq=fetal_cardiac_frequency, professional_id=professional.id, internment_id=internment.id)
    db.session.add(measure)
    db.session.commit()

    return measure
