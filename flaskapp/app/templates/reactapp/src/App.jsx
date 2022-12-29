import Router from "./routes";
import { GlobalStyles } from "./theme/styles.App";
import theme from "./theme/theme";

import React from "react";
import { ThemeProvider } from "styled-components";
import { ApolloProvider } from "@apollo/client";
import client from "config/apollo";
import { SnackbarProvider } from "notistack";

function App() {
  return (
    <SnackbarProvider maxSnack={3}>
      <ApolloProvider client={client}>
        <ThemeProvider theme={theme}>
          <GlobalStyles />
          <Router />
        </ThemeProvider>
      </ApolloProvider>
    </SnackbarProvider>
  );
}
export default App;
