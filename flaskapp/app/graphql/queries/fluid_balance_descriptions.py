from app.graphql import query
from app.models import db, FluidBalanceDescription

@query.field("fluidBalanceDescriptions")
def fluid_balance_descriptions(*_):
    return db.session.query(FluidBalanceDescription).all()