import ModalAddPrescription from "components/Modals/components/ModalsPrescription/components/ModalPrescription";

const addPrescription = ({ confirmButtonAction }) => ({
  confirmButtonAction: confirmButtonAction,
  content: <ModalAddPrescription />,
  returnButtonAction: () => {},
  title: "Adicionar Nova Linha",
});

export default addPrescription;
