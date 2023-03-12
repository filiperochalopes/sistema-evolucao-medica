from app.graphql import query
from app.serializers import UserSchema
from app.services.utils.decorators import token_authorization

@query.field('myUser')
@token_authorization
def my_user(*_, current_user:dict):
    schema =  UserSchema()
    return schema.dump(current_user)