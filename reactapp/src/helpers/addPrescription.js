import ModalAddPrescription from "components/Modals/components/ModalsPrescription/components/ModalPrescription";

const addPrescription = ({
  confirmButtonAction,
  drugs,
  nursingActivities,
  currentMedicament,

  notChangeType = false,
}) => ({
  confirmButtonAction: confirmButtonAction,
  content: (
    <ModalAddPrescription
      drugs={drugs}
      nursingActivities={nursingActivities}
      currentMedicament={currentMedicament}
      notChangeType={notChangeType}
    />
  ),
  returnButtonAction: () => {},
  title: notChangeType ? "Atualizar Linha" : "Adicionar Nova Linha",
});

export default addPrescription;
