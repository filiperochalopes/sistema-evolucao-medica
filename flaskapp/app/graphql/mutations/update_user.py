from ariadne import convert_kwargs_to_snake_case
from app.models import db
from app.graphql import mutation
from app.models import User
from app.serializers import UserSchema
from app.services.utils.auth import cpf_validator, cns_validator
from app.services.utils.decorators import token_authorization   
import sys

@mutation.field('updateMyUser')
@token_authorization
@convert_kwargs_to_snake_case
def update_my_user(_, info, user: dict, current_user:dict):
    # Realizando encriptação de senha
    if 'password' in user:
        encrypted_password = User.generate_password(user['password'])
        del user['password']
        user['password_hash'] = encrypted_password
    # Verifica o preenchimento de cpf ou cns, um dos dois devem estar preenchidos
    if not user['cpf'] and not user['cns']:
        raise Exception(
            'CPF ou CNS devem estar preenchidos, os dois campos não podem ficar em branco')
    if user['cns'] is not None:
        if cns_validator.validate(user['cns']) is False:
            raise Exception('Número de CNS inválido')
    if user['cpf'] is not None:
        if cpf_validator.validate(user['cpf']) is False:
            raise Exception('Número de CPF inválido')

    user_model = db.session.query(User).get(current_user.id)
    for key, value in user.items():     
        setattr(user_model, key, value)
    print(user_model, file=sys.stderr)
    print(user, file=sys.stderr)
    db.session.commit()

    schema =  UserSchema()
    return schema.dump(user_model)
