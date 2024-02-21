import PageTemplate from "../layouts/Page";
import Login from "../views/Login";

import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Outlet } from "react-router-dom";
import ModalContextProvider from "services/ModalContext";
import EditUser from "views/EditUser";
import Admit from "views/Pacient/Admit";
import Chart from "views/Pacient/Chart";
import Evolution from "views/Pacient/Evolution";
import List from "views/Pacient/List";
import VitalSign from "views/Pacient/VitalSigns";
import PrivateRouter from "./PrivateRouter";
import CheckRole from "./CheckRole";
import ContextProvider from "services/Context";

export const routes = [
  {
    path: "/",
    element: (
      <ContextProvider>
        <ModalContextProvider>
          <PageTemplate>
            <Outlet />
          </PageTemplate>
        </ModalContextProvider>
      </ContextProvider>
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
            <CheckRole goBack roles={["doc"]}>
              <Admit />
            </CheckRole>
          </PrivateRouter>
        ),
      },
      {
        path: "/editar-usuario",
        element: (
          <PrivateRouter>
            <CheckRole goBack roles={["doc"]}>
              <EditUser />
            </CheckRole>
          </PrivateRouter>
        ),
      },
      {
        path: "/evoluir-paciente/:id",
        element: (
          <PrivateRouter>
            <CheckRole goBack roles={["doc", "nur"]}>
              <Evolution />
            </CheckRole>
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
        path: "/prontuario/:id",
        element: (
          <PrivateRouter>
            <Chart />
          </PrivateRouter>
        ),
      },
    ],
  },
];

const routers = createBrowserRouter(routes);

function Router() {
  return <RouterProvider router={routers} />;
}

export default Router;
