from app.graphql import query

@query.field("cid10")
def fixtures(*_):
    return []