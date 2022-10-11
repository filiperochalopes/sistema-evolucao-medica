import PageTemplate from "../layouts/Page";
import Login from "../views/Login";

import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Outlet } from "react-router-dom";
import List from "views/Pacient/List";

const routers = createBrowserRouter([
  {
    path: "/",
    element: (
      <PageTemplate>
        <Outlet />
      </PageTemplate>
    ),
    children: [
      {
        path: "/",
        element: <Login />,
      },
      {
        path: "/pacients",
        element: <List />,
      },
    ],
  },
]);

function Router() {
  return <RouterProvider router={routers} />;
}

export default Router;
