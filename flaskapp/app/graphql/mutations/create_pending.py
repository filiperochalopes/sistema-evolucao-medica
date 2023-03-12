from ariadne import convert_kwargs_to_snake_case

import sys
from app.graphql import mutation
from app.models import db, Internment, Pending
from app.services.utils.decorators import token_authorization

@mutation.field('createPending')
@convert_kwargs_to_snake_case
@token_authorization
def create_pending(_, info, internment_id:int, text:str, current_user: dict):
    # Determinando internamento
    internment = db.session.query(Internment).get(internment_id)
    # Determinando profissional que está registrando
    professional = current_user
    # Verifica se está igual à última pendência cadastrada
    last_pending = db.session.query(Pending).filter(Pending.internment_id==internment_id).order_by(Pending.created_at.desc()).first()
    
    if last_pending.text == text:
        raise Exception("A pendência não pode ser cópia idêntica do registro anterior")
    # Cria o registro de pendências, que não está atrelada a uma evolução
    pendings = Pending(text=text, internment_id=internment.id, professional_id=professional.id)
    db.session.add(pendings)
    db.session.commit()
    
    return pendings
