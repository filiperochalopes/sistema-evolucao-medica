from datetime import datetime

from ariadne import convert_kwargs_to_snake_case
from app.models import db
from app.env import MASTER_KEY
from app.graphql import mutation
from app.models import User, ProfessionalCategoryEnum
from app.serializers import UserSchema
from app.services.utils.auth import cpf_validator, cns_validator


@mutation.field('createUser')
@convert_kwargs_to_snake_case
def create_user(_, info, master_key: str, user: dict):
    if master_key == MASTER_KEY:
        # Cria um usuário em model
        encrypted_password = User.generate_password(user['password'])
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

        # Administrador não tem registro em Conselho da profissão
        if user['professional_category'] == 'adm':
            professional_document_uf = None
            professional_document_number = None
        else:
            professional_document_uf = user['professional_document_uf']
            professional_document_number = user['professional_document_number']

        new_user = User(
            name=user['name'], 
            email=user['email'], 
            phone=user['phone'],
            birthdate=datetime.strptime(user['birthdate'], '%Y-%m-%d'),
            password_hash=encrypted_password, 
            cpf=user['cpf'], 
            cns=user['cns'],
            professional_category=ProfessionalCategoryEnum[user['professional_category']],
            professional_document_uf=professional_document_uf,
            professional_document_number=professional_document_number
        )
        db.session.add(new_user)
        db.session.commit()
    else:
        raise Exception(
            'Você não tem permissões para entrar nessa rota, entre com uma masterKey correta')

    schema =  UserSchema()
    return schema.dump(new_user)
