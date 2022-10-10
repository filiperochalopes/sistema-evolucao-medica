from ariadne import gql, QueryType

# Define type definitions (schema) using SDL
type_defs = gql("""
    type Query {
       users: [User]
    }

    type Mutation {
        signin(email:String!, password:String!)
    }


   type User {
       username: String
       email: String
       password: String
    }  

    type Patient {
        name: String
        cns: Int
    }
""")

# Initialize query
query = QueryType()
