from ariadne import gql, QueryType

# Define type definitions (schema) using SDL
type_defs = gql("""
    type Query {
       users: [User]
       cid10: [Cid10!]
    }

    type Mutation {
        signin(email:String!, password:String!): User
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

    type Cid10 {
        code: String!
        description: String!
    }
""")

# Initialize query
query = QueryType()
