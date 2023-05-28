from app.graphql import query
from app.models import db, HighComplexityProcedure

# TODO Criar depois priorização para que apareçam primeiro em ordem os procedimentos mais utilizados
@query.field("highComplexityProcedures")
def high_complexity_procedures(*_):
    return db.session.query(HighComplexityProcedure).all()