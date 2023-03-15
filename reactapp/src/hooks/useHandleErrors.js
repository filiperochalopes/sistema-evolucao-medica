const { useSnackbar } = require("notistack");

const useHandleErrors = () => {
  const { enqueueSnackbar } = useSnackbar();

  const handleErrors = (error) => {
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
