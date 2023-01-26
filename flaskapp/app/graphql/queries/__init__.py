import sqlalchemy as sa
from sqlalchemy import create_engine
from app.env import DatabaseSettings

from app.graphql import query
import app.graphql.queries.patient
import app.graphql.queries.state
import app.graphql.queries.cid10
import app.graphql.queries.prescription
import app.graphql.queries.internments
import app.graphql.queries.internment
import app.graphql.queries.procedures
import app.graphql.queries.my_user
import app.graphql.queries.fluid_balance_descriptions


@query.field("hello")
def hello(*_):
    return "World!"

@query.field("alembicVersion")
def get_alembic_version(*_):
    engine = create_engine(DatabaseSettings().URL)
    with engine.begin() as conn:
        q = sa.text("SELECT version_num FROM alembic_version")
        resultset = conn.execute(q)
        results_as_dict = resultset.mappings().all()
    return {
        "version": results_as_dict[0]['version_num']
    }