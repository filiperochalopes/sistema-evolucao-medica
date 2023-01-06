from ariadne import convert_kwargs_to_snake_case
import bcrypt

from app.graphql import mutation
from app.models import db, User
from app.utils.decorators import token_authorization
from app.serializers import UserSchema

@mutation.field('updatePassword')
@convert_kwargs_to_snake_case
@token_authorization
def update_password(_, info, password:str, current_user:dict):
    user = db.session.query(User).get(current_user['id'])
    encrypted_password = User.generate_password(password)
    user.password = encrypted_password
    db.session.commit()
    
    schema = UserSchema()
    return schema.dump(user)
