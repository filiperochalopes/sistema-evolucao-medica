import Button from "components/Button";
import { useState } from "react";
import { Link } from "react-router-dom";
import CheckRole from "routes/CheckRole";
import Container, { PopUp } from "./styles";

const EvolutionButton = ({ id }) => {
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
          <CheckRole roles={["doc", "nur"]}>
            <Link to={`/evoluir-paciente/${id}`}>Adicionar evolução</Link>
          </CheckRole>

          <Link to={`/sinais-vitais/${id}`}>Atualizar sinais vitais</Link>
        </PopUp>
      )}
    </Container>
  );
};

export default EvolutionButton;
