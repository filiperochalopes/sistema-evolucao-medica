import PageTemplate from "../layouts/Page";
import Login from "../views/Login";

import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Outlet } from "react-router-dom";
import Admit from "views/Pacient/Admit";
import Evolution from "views/Pacient/Evolution";
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
        path: "/pacientes",
        element: <List />,
      },
      {
        path: "/adimitir-paciente",
        element: <Admit />,
      },
      {
        path: "/evoluir-paciente",
        element: <Evolution />,
      },
    ],
  },
]);

function Router() {
  return <RouterProvider router={routers} />;
}

export default Router;
