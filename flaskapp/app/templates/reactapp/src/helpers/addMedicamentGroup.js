import ModalMedicamentGroup from "components/Modals/components/ModalsPrescription/components/ModalMedicamentsGroup";

const addMedicamentGroup = ({
  confirmButtonAction,
  currentMedicament = [],
}) => ({
  confirmButtonAction: confirmButtonAction,
  content: <ModalMedicamentGroup currentMedicament={currentMedicament} />,
  returnButtonAction: () => {},
  title: "Adicionar Grupo de Prescrição",
});

export default addMedicamentGroup;
