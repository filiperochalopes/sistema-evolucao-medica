import PageTemplate from "../layouts/Page";
import Login from "../views/Login";

import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Outlet } from "react-router-dom";
import ModalContextProvider from "services/ModalContext";
import Admit from "views/Pacient/Admit";
import Chart from "views/Pacient/Chart";
import Evolution from "views/Pacient/Evolution";
import List from "views/Pacient/List";
import VitalSign from "views/Pacient/VitalSigns";

const routers = createBrowserRouter([
  {
    path: "/",
    element: (
      <ModalContextProvider>
        <PageTemplate>
          <Outlet />
        </PageTemplate>
      </ModalContextProvider>
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
        path: "/evoluir-paciente/:id",
        element: <Evolution />,
      },
      {
        path: "/sinais-vitais/:id",
        element: <VitalSign />,
      },
      {
        path: "/prontuario",
        element: <Chart />,
      },
    ],
  },
]);

function Router() {
  return <RouterProvider router={routers} />;
}

export default Router;
