import Button from "components/Button";
import Container from "./styles";

const ModalDeletePrescription = ({ confirmButton, goBack }) => (
  <Container>
    <p>Tem certeza que deseja remover esse item da prescrição?</p>
    <div>
      <Button type="button" customType="gray" onClick={confirmButton}>
        Sim
      </Button>
      <Button type="button" customType="red" onClick={goBack}>
        Não
      </Button>
    </div>
  </Container>
);

export default ModalDeletePrescription;
