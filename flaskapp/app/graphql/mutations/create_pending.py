from ariadne import convert_kwargs_to_snake_case

from app.graphql import mutation
from app.models import db, Internment, Pending
from app.utils.decorators import token_authorization

@mutation.field('createPending')
@convert_kwargs_to_snake_case
@token_authorization
def create_pending(_, info, internment_id:int, text:str, current_user: dict):
    # Determinando internamento
    internment = db.session.query(Internment).get(internment_id)
    # Determinando profissional que está registrando
    professional = current_user

    # Cria o registro de pendências, que não está atrelada a uma evolução
    pendings = Pending(text=text, internment_id=internment.id, professional_id=professional.id)
    db.session.add(pendings)
    db.session.commit()
    
    return pendings
