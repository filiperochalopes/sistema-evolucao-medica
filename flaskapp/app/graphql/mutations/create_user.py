from datetime import datetime
from pprint import pprint
import bcrypt
import sys

from ariadne import convert_kwargs_to_snake_case
from app.models import db
from app.env import MASTER_KEY
from app.graphql import mutation
from app.models import User, ProfessionalCategoryEnum
from app.serializers import UserSchema
from app.utils.functions import cpf_validator, cns_validator


@mutation.field('createUser')
@convert_kwargs_to_snake_case
def create_user(_, info, master_key: str, user: dict):
    print('Hello World', file=sys.stderr)
    print(master_key, file=sys.stderr)
    print(MASTER_KEY, file=sys.stderr)
    if master_key == MASTER_KEY:
        # Cria um usuário em model
        encrypted_password = bcrypt.hashpw(
            user['password'].encode('utf-8'), bcrypt.gensalt())
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

        pprint(user)
        print(ProfessionalCategoryEnum['doc'], file=sys.stderr)
        new_user = User(
            name=user['name'], 
            email=user['email'], 
            phone=user['phone'],
            birthday=datetime.strptime(user['birthday'], '%Y-%m-%d'),
            password_hash=encrypted_password, 
            cpf=user['cpf'], 
            cns=user['cns'],
            professional_category=ProfessionalCategoryEnum[user['professional_category']],
            professional_document_uf=user['professional_document_uf'],
            professional_document_number=user['professional_document_number']
        )
        db.session.add(new_user)
        db.session.commit()
        print(new_user.__dict__, file=sys.stderr)
    else:
        raise Exception(
            'Você não tem permissões para entrar nessa rota, entre com uma masterKey correta')

    schema =  UserSchema()
    return schema.dump(new_user)
