from app.graphql import query
from app.models import db, State

@query.field("state")
def state(*_):
    return db.session.query(State).order_by(State.name.asc()).all()