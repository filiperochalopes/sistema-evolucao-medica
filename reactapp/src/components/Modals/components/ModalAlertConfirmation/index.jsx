import Button from "components/Button";
import Container from "./styles";

const ModalAlertConfirmation = ({ question, confirmCallback, goBack }) => (
  <Container>
    <p>{question}</p>
    <div>
      <Button type="button" customType="gray" onClick={confirmCallback}>
        Sim
      </Button>
      <Button type="button" customType="red" onClick={goBack}>
        Não
      </Button>
    </div>
  </Container>
);

export default ModalAlertConfirmation;
