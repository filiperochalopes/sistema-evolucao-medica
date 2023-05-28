import { useContextProvider } from "services/Context";

const { Navigate, useLocation } = require("react-router-dom");

const PrivateRouter = ({ children }) => {
  const { decodedJWT } = useContextProvider();
  const location = useLocation();
  if (
    (location.pathname !== "/" && !localStorage.getItem("token")) ||
    new Date() > new Date(decodedJWT?.exp * 1000)
  ) {
    return <Navigate to="/" replace />;
  }
  return children;
};

export default PrivateRouter;
