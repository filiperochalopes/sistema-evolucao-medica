from datetime import datetime
import sys

from ariadne import convert_kwargs_to_snake_case

from app.serializers import EvolutionSchema
from app.graphql import mutation
from app.models import db, Internment, Evolution
from app.utils.decorators import token_authorization

@mutation.field('createEvolution')
@convert_kwargs_to_snake_case
@token_authorization
def create_evolution(_, info, internment_id:int, text:str, cid_10_code: str, current_user: dict):
    # Determinando internamento
    internment = db.session.query(Internment).get(internment_id)
    # Determinando profissional que está registrando
    professional = current_user

    # Cria a evolução textual
    evolution = Evolution(text=text, professional_id=professional.id, internment_id=internment.id, cid10_code=cid_10_code)
    db.session.add(evolution)

    db.session.commit()
    schema = EvolutionSchema()

    return schema.dump(evolution)
