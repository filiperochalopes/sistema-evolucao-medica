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
import PrivateRouter from "./PrivateRouter";

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
        element: (
          <PrivateRouter>
            <List />
          </PrivateRouter>
        ),
      },
      {
        path: "/adimitir-paciente",
        element: (
          <PrivateRouter>
            <Admit />
          </PrivateRouter>
        ),
      },
      {
        path: "/evoluir-paciente/:id",
        element: (
          <PrivateRouter>
            <Evolution />
          </PrivateRouter>
        ),
      },
      {
        path: "/sinais-vitais/:id",
        element: (
          <PrivateRouter>
            <VitalSign />
          </PrivateRouter>
        ),
      },
      {
        path: "/prontuario",
        element: (
          <PrivateRouter>
            <Chart />
          </PrivateRouter>
        ),
      },
    ],
  },
]);

function Router() {
  return <RouterProvider router={routers} />;
}

export default Router;
