from app.graphql import query

@query.field("patients")
def fixtures(*_, cns=None):
    return []
