import Button from "components/Button";
import { useState } from "react";
import { Link } from "react-router-dom";
import Container, { PopUp } from "./styles";

const EvolutionButton = () => {
  const [showPopUp, setShowPopUp] = useState(false);

  return (
    <Container>
      <Button
        customType="gray"
        type="button"
        onClick={() => setShowPopUp(!showPopUp)}
      >
        Evoluir
      </Button>
      {showPopUp && (
        <PopUp>
          <Link to="/evoluir-paciente">Adicionar evolução</Link>

          <Link to="/sinais-vitais">Atualizar sinais vitais</Link>
        </PopUp>
      )}
    </Container>
  );
};

export default EvolutionButton;
