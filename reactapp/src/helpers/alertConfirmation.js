import ModalAlertConfirmation from "components/Modals/components/ModalAlertConfirmation";

const alertConfirmation = ({ confirmCallback, question }) => ({
  confirmButtonAction: confirmCallback,
  content: <ModalAlertConfirmation />,
  returnButtonAction: () => {},
  question,
  title: "Atenção",
  headerStyle: "red",
});

export default alertConfirmation;
