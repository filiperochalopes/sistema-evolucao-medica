import Router from "./routes";
import { GlobalStyles } from "./theme/styles.App";
import theme from "./theme/theme";

import React from "react";
import { ThemeProvider } from "styled-components";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyles />
      <Router />
    </ThemeProvider>
  );
}
export default App;
