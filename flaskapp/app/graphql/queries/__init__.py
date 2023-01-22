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
