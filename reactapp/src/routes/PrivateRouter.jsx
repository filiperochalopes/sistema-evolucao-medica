const { Navigate, useLocation } = require("react-router-dom");

const PrivateRouter = ({ children }) => {
  const location = useLocation();
  if (location.pathname !== "/" && !localStorage.getItem("token")) {
    return <Navigate to="/" replace />;
  }
  return children;
};

export default PrivateRouter;
