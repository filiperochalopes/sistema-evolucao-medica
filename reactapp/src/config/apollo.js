import {
  ApolloClient,
  createHttpLink,
  InMemoryCache,
  ApolloLink,
} from "@apollo/client";
import { setContext } from "@apollo/client/link/context";
import { onError } from "@apollo/client/link/error";
import fetch from "cross-fetch";
const httpLink = createHttpLink({
  uri: "/api/v1/graphql",
  fetch,
});

const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem("token");
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : "",
    },
  };
});

const logoutLink = onError(({ response }) => {
  if (
    response?.errors?.find((error) => error.message === "Signature has expired")
  ) {
    localStorage.removeItem("token");
    window.location.href = "/";
  }
});

const client = new ApolloClient({
  link: ApolloLink.from([logoutLink, authLink, httpLink]),
  cache: new InMemoryCache(),
});

export default client;
