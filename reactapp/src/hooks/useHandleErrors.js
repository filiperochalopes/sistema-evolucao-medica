const { useSnackbar } = require("notistack");

const useHandleErrors = () => {
  const { enqueueSnackbar } = useSnackbar();

  const handleErrors = (error) => {
    if (error?.message === "Failed to fetch") {
      enqueueSnackbar("Erro de Conexão, tente novamente", { variant: "error" });
      return;
    }
    if (error.graphQLErrors) {
      error.graphQLErrors.forEach((err) => {
        enqueueSnackbar(err.message, { variant: "error" });
      });
    } else {
      enqueueSnackbar("Erro,tente novamente", { variant: "error" });
    }
  };

  return { handleErrors };
};

export default useHandleErrors;
