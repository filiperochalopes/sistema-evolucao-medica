import PageTemplate from "../layouts/Page";
import Login from "../views/Login";

import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const routers = createBrowserRouter([
  {
    path: "/",
    element: <PageTemplate />,
    children: [
      {
        path: "/",
        element: <Login />,
      },
    ],
  },
]);

function Router() {
  return <RouterProvider router={routers} />;
}

export default Router;
