from app.graphql import query
from app.models import db, HighComplexityProcedure

@query.field("highComplexityProcedures")
def high_complexity_procedures(*_):
    return db.session.query(HighComplexityProcedure).all()