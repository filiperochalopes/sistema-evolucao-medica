import ModalAddPrescription from "components/Modals/components/ModalsPrescription/components/ModalPrescription";

const addPrescription = ({
  confirmButtonAction,
  drugs,
  nursingActivities,
}) => ({
  confirmButtonAction: confirmButtonAction,
  content: (
    <ModalAddPrescription drugs={drugs} nursingActivities={nursingActivities} />
  ),
  returnButtonAction: () => {},
  title: "Adicionar Nova Linha",
});

export default addPrescription;
