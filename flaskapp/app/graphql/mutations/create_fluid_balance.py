from ariadne import convert_kwargs_to_snake_case

from app.graphql import mutation
from app.models import db, Internment, FluidBalance, FluidBalanceDescription
from app.serializers import FluidBalanceSchema
from app.services.utils.decorators import token_authorization

@mutation.field('createFluidBalance')
@convert_kwargs_to_snake_case
@token_authorization
def create_fluid_balance(_, info, internment_id: int, volume_ml: int, description: str, current_user: dict):
    # Determinando internamento
    internment = db.session.query(Internment).get(internment_id)
    # Determinando profissional que está registrando
    professional = current_user

    # Cria o registro de balanço hídrico
    fluid_balance = FluidBalance(volume_ml=volume_ml, professional_id=professional.id, internment_id=internment.id)
    db.session.add(fluid_balance)
    
    # Cria ou seleciona a descrição de balanço hídrico
    try:
        fluid_balance_description = db.session.query(FluidBalanceDescription).filter(FluidBalanceDescription.value == description).one()
    except Exception:
        fluid_balance_description = FluidBalanceDescription(value=description)
        db.session.add(fluid_balance_description)
        db.session.flush()    

    fluid_balance.description = fluid_balance_description
    db.session.commit()
    
    schema = FluidBalanceSchema()

    return schema.dump(fluid_balance)
