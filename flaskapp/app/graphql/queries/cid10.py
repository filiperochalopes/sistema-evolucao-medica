from app.graphql import query
from app.models import db, Cid10

@query.field("cid10")
def cid10(*_):
    return db.session.query(Cid10).all()