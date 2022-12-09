from app.graphql import query
from app.utils.decorators import token_authorization

@query.field('myUser')
@token_authorization
def my_user(*_, current_user:dict):
    return current_user