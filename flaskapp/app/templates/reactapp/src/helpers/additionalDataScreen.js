import ModalAdditionalData from "components/Modals/components/ModalAdditionalData";

const additionalDataScreen = ({ type = "hospitalAdmissionForm" }) => ({
  confirmButtonAction: () => {},
  content: <ModalAdditionalData type={type} />,
  returnButtonAction: () => {},
  title: "Preencha os campos adicionais",
});

export default additionalDataScreen;
