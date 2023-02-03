import ModalAddPrescription from "components/Modals/components/ModalsPrescription/components/ModalPrescription";

const addPrescription = ({
  confirmButtonAction,
  drugs,
  nursingActivities,
  currentMedicament,
}) => ({
  confirmButtonAction: confirmButtonAction,
  content: (
    <ModalAddPrescription
      drugs={drugs}
      nursingActivities={nursingActivities}
      currentMedicament={currentMedicament}
    />
  ),
  returnButtonAction: () => {},
  title: "Adicionar Nova Linha",
});

export default addPrescription;
