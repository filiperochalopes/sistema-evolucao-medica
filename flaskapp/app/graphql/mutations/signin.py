from datetime import datetime
import sys
import bcrypt
import jwt
import datetime

from ariadne import convert_kwargs_to_snake_case
from app.env import SECRET, TOKEN_HOUR_EXPIRATION

from app.graphql import mutation
from app.models import User, db
from app.serializers import UserSchema


@mutation.field('signin')
@convert_kwargs_to_snake_case
def create_user(_, info, email: str, password: str):
    try:
        user = db.session.query(User).filter(User.email==email).one()
    except Exception as e:
        raise Exception(f'{e} Não existe usuário com esse email')

    print(user.__dict__, file=sys.stderr)

    # Cria um usuário em model
    if(bcrypt.checkpw(password.encode('utf-8'), user.password_hash)):
        encoded_jwt = jwt.encode({
            'sub': user.id,
            'scope': user.professional_category.name,
            'exp': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=TOKEN_HOUR_EXPIRATION)
        }, SECRET, algorithm="HS256")
    else:
        raise Exception('Senha inválida')

    schema = UserSchema()
    return {
        'user': schema.dump(user),
        'token': encoded_jwt
    }
