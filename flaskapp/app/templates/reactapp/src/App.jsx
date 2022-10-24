import Router from "./routes";
import { GlobalStyles } from "./theme/styles.App";
import theme from "./theme/theme";

import React from "react";
import { ThemeProvider } from "styled-components";
import { ApolloProvider } from "@apollo/client";
import client from "config/apollo";

function App() {
  return (
    <ApolloProvider client={client}>
      <ThemeProvider theme={theme}>
        <GlobalStyles />
        <Router />
      </ThemeProvider>
    </ApolloProvider>
  );
}
export default App;
