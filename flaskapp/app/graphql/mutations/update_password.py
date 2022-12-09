from ariadne import convert_kwargs_to_snake_case
import bcrypt

from app.graphql import mutation
from app.models import db, User
from app.utils.decorators import token_authorization
from app.serializers import UserSchema

@mutation.field('updatePassword')
@convert_kwargs_to_snake_case
@token_authorization
def update_password(_, info, id:str, password:str):
    user = db.session.query(User).get(id)
    encrypted_password = bcrypt.hashpw(
        password.encode('utf-8'), bcrypt.gensalt())
    user.password = encrypted_password
    db.session.commit()
    
    schema = UserSchema()
    return schema.dump(user)
