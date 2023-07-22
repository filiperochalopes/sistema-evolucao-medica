import ModalDeletePrescription from "components/Modals/components/ModalsPrescription/components/ModalDeletePrescription";

const deletePrescription = ({ confirmButtonAction }) => ({
  confirmButtonAction: confirmButtonAction,
  content: <ModalDeletePrescription />,
  returnButtonAction: () => {},
  title: "Atenção",
  headerStyle: "red",
});

export default deletePrescription;
