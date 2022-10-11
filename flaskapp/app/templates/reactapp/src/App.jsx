import Router from "./routes";
import GlobaStyles from "./theme/globaStyles";
import theme from "./theme/theme";

import React from "react";
import { ThemeProvider } from "styled-components";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <GlobaStyles />
      <Router />
    </ThemeProvider>
  );
}
export default App;
