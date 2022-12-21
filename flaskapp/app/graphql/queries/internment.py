from app.graphql import query
from app.models import Internment, db
from app.serializers import InternmentSchema

@query.field("internment")
def internment(*_, id:int):
    '''Captura os dados completos de internamento'''
    schema = InternmentSchema()
    return schema.dump(db.session.query(Internment).get(id))