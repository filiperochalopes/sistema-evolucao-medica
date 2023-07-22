import ModalAddPrescription from "components/Modals/components/ModalsPrescription/components/ModalPrescription";

const addPrescription = ({
  confirmButtonAction,
  drugs,
  nursingActivities,
  currentPrescription,
  update = false,
}) => ({
  confirmButtonAction,
  content: (
    <ModalAddPrescription
      drugs={drugs}
      nursingActivities={nursingActivities}
      currentPrescription={currentPrescription}
      update={update}
    />
  ),
  returnButtonAction: () => {},
  title: update ? "Atualizar Linha" : "Adicionar Nova Linha",
});

export default addPrescription;
