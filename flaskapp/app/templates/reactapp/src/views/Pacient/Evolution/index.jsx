import Container from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import ListOption from "components/ListOption";
import TextArea from "components/TextArea";

const Evolution = () => (
  <Container>
    <div>
      <div>
        <h2>Evoluir Paciente (João Miguel dos Santos Polenta, 83 anos)</h2>
        <Button>Atualizar Dados do Paciente</Button>
      </div>
      <TextArea placeholder="EVOLUÇÃO" />
      <div className="row">
        <Input placeholder="RESPONSÁVEL PELA EVOLUÇÃO (NOME COMPLETO)" />
        <Input placeholder="FUNÇÃO" />
        <Input placeholder="N° CONSELHO" />
      </div>
      <Input placeholder="CID - SUSPEITA INICIAL" />

      <Button>Evoluir</Button>
    </div>

    <div>
      <h2>Prescrição</h2>
      <ol>
        <li>
          <ListOption>REPOUSO RELATIVO NO LEITO À 30°</ListOption>
        </li>
      </ol>
      <div></div>
      <Button>Atualizar prescrição</Button>
    </div>
    <div>
      <h2>Pendências</h2>
      <TextArea placeholder="AQUI SEGUE UM TEXTO COM AS PENDÊNCIAS"></TextArea>
      <Button>Atualizar Pendências</Button>
    </div>
  </Container>
);

export default Evolution;
