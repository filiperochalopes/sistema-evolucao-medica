from ariadne import gql, QueryType, load_schema_from_path

# Define type definitions (schema) using SDL
type_defs = gql(
    """
    type Query {
        cid10: [Cid10!]
    }

    type Cid10 {
        code: String!
        description: String!
    }
   """
)

# Initialize query
query = QueryType()
