import Container from "./styles";

import Button from "components/Button";
import { FormikInput } from "components/Input";
import React from "react";
import { useFormik } from "formik";
import { UPDATE_MY_USER } from "graphql/mutations";
import { useMutation } from "@apollo/client";
import { useEffect } from "react";
import validationSchema from "./schema";
import maskCpf from "utils/maskCpf";
import { useSnackbar } from "notistack";
import useHandleErrors from "hooks/useHandleErrors";
import { useContextProvider } from "services/Context";

const EditUserPage = () => {
  const [updateUser] = useMutation(UPDATE_MY_USER);
  const { enqueueSnackbar } = useSnackbar();
  const { handleErrors } = useHandleErrors();
  const { user, updateUser: contextUpdateUser } = useContextProvider();

  const formik = useFormik({
    initialValues: {
      name: "",
      email: "",
      cns: "",
      cpf: "",
      birthdate: "",
      password: "",
      passwordConfirmation: "",
    },
    onSubmit: async (values) => {
      try {
        console.log(values);
        let updatePassword = false;
        if (values.passwordConfirmation) {
          updatePassword = true;
        } else {
          delete values.password;
        }
        // Excluindo campos desnecessarios
        delete values.passwordConfirmation;
        delete values.__typename;
        delete values.id;
        console.log(values);
        await updateUser({
          variables: {
            user: values,
          },
        });
        // Atualiza usuário no contexto
        contextUpdateUser();
        if (updatePassword)
          enqueueSnackbar("Senha Atualizada", { variant: "success" });
        enqueueSnackbar("Usuário Atualizado", { variant: "success" });
      } catch (e) {
        console.log(e);
        handleErrors(e);
      }
    },
    validationSchema,
  });

  useEffect(() => {
    if (user) {
      console.log(user);
      formik.setValues({
        ...user,
      });
    }
  }, [user]);

  return (
    <Container>
      <h2>Editar Usuário</h2>
      <form onSubmit={formik.handleSubmit}>
        <div className="row">
          <FormikInput formik={formik} name="name" label="Nome" />
          <FormikInput
            formik={formik}
            name="email"
            label="Email"
            disabled={true}
          />
          <FormikInput
            formik={formik}
            name="birthdate"
            label="Data de Nascimento"
            type="date"
          />
        </div>
        <div className="row">
          <FormikInput formik={formik} name="cns" label="CNS" />
          <FormikInput
            formik={formik}
            name="cpf"
            label="CPF"
            onChange={(e) => maskCpf(e.target.value)}
          />
        </div>
        <div className="row">
          <FormikInput
            formik={formik}
            name="password"
            label="Senha"
            type="password"
          />

          <FormikInput
            formik={formik}
            name="passwordConfirmation"
            type="password"
            label="Confirmação de Senha"
          />
        </div>
        <Button type="submit" className="small">
          Atualizar
        </Button>
      </form>
    </Container>
  );
};

export default EditUserPage;
