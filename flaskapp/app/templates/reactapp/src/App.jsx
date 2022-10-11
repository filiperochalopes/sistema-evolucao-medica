import Router from "./routes";
import { GlobalStyles } from "./theme/styles.App";
import theme from "./theme/theme";

import React from "react";
import ModalContextProvider from "services/ModalContext";
import { ThemeProvider } from "styled-components";

function App() {
  return (
    <ModalContextProvider>
      <ThemeProvider theme={theme}>
        <GlobalStyles />
        <Router />
      </ThemeProvider>
    </ModalContextProvider>
  );
}
export default App;
