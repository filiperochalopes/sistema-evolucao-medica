import { MockedProvider } from "@apollo/client/testing";
import "@testing-library/jest-dom";
import { act, fireEvent, render, screen } from "@testing-library/react";
import { SIGNING } from "../../graphql/mutations";
import React from "react";
import App from "App";
import { SnackbarProvider } from "notistack";
import { ThemeProvider } from "styled-components";
import { GlobalStyles } from "theme/styles.App";
import Router, { routes } from "routes";
import theme from "theme/theme";
import { createMemoryRouter, RouterProvider } from "react-router-dom";
const mocks = [
  {
    request: {
      query: SIGNING,
      variables: {
        email: "lucas@gmail.com",
        password: "12345678",
      },
    },
    result: {
      data: {
        signin: {
          token:
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjUsInNjb3BlIjoiZG9jIiwiZXhwIjoxNjgxMjM1OTk0fQ.vT-oKmssmL7O6UMcvu8j5NA8ovHatq3RKqk4YPDYpfM",
        },
      },
    },
  },
]; // We'll fill this in next
describe("doctor flux", () => {
  it("login", async () => {
    const router = createMemoryRouter(routes, {
      initialEntries: ["/"],
      initialIndex: 0,
    });
    // process.env.REACT_APP_API_URL =
    //   "https://hmlem.aguafria.filipelopes.med.br/api/v1";
    act(() => {
      render(
        <MockedProvider mocks={mocks} addTypename={false}>
          <SnackbarProvider autoHideDuration={3000} maxSnack={3}>
            <ThemeProvider theme={theme}>
              <GlobalStyles />
              <RouterProvider router={router} />
            </ThemeProvider>
          </SnackbarProvider>
        </MockedProvider>
      );
    });
    const emailInput = screen.getByTestId("email");
    const passwordInput = screen.getByTestId("password");
    const button = screen.getByTestId("button");
    act(() => {
      fireEvent.change(emailInput, { target: { value: "lucas@gmail.com" } });
    });
    act(() => {
      fireEvent.change(passwordInput, { target: { value: "12345678" } });
    });
    act(() => {
      fireEvent.click(button);
    });
    expect(await screen.findByText("Pacientes Internados")).toBeInTheDocument();
    // const text = screen.getByText("Pacientes Internados");
  });
});
