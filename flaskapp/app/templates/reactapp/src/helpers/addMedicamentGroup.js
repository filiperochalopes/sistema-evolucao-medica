import ModalMedicamentGroup from "components/Modals/components/ModalsPrescription/components/ModalMedicamentsGroup";

const addMedicamentGroup = ({ confirmButtonAction }) => ({
  confirmButtonAction: confirmButtonAction,
  content: <ModalMedicamentGroup />,
  returnButtonAction: () => {},
  title: "Adicionar Grupo de Prescrição",
});

export default addMedicamentGroup;
