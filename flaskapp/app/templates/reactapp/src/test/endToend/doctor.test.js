import { MockedProvider } from "@apollo/client/testing";
import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { SIGNING } from "../../graphql/mutations";
import React from "react";
import App from "App";
const mocks = [
  {
    request: {
      query: SIGNING,
      variables: {
        name: "Buck",
      },
    },
    result: {
      data: {
        dog: { id: "1", name: "Buck", breed: "bulldog" },
      },
    },
  },
]; // We'll fill this in next
test("doctor flux", () => {
  render(
    <MockedProvider mocks={mocks} addTypename={false}>
      <App />
    </MockedProvider>
  );
});
