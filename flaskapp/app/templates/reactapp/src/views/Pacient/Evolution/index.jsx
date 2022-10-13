import Container from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import ListOption from "components/ListOption";
import TextArea from "components/TextArea";

const Evolution = () => (
  <Container>
    <div className="evolution_pacient">
      <div className="header">
        <h2>Evoluir Paciente (João Miguel dos Santos Polenta, 83 anos)</h2>
        <Button>Atualizar Dados do Paciente</Button>
      </div>
      <TextArea placeholder="EVOLUÇÃO" />
      <div className="row">
        <Input
          placeholder="RESPONSÁVEL PELA EVOLUÇÃO (NOME COMPLETO)"
          className="larger"
        />
        <Input placeholder="FUNÇÃO" className="normal" />
        <Input placeholder="N° CONSELHO" className="small" />
      </div>
      <div>
        <Input placeholder="CID - SUSPEITA INICIAL" />
        <p className="legend">
          ÚLTIMA EVOLUÇÃO ATUALIZADA POR FULANO EM DD/MM/AAAA HH:DD
        </p>
      </div>

      <Button className="evolution_button">Evoluir</Button>
    </div>

    <div className="prescriptions_pacient">
      <h2>Prescrição</h2>
      <ol>
        <li>
          <ListOption>REPOUSO RELATIVO NO LEITO À 30°</ListOption>
        </li>
        <li>
          <ListOption>REPOUSO RELATIVO NO LEITO À 30°</ListOption>
        </li>
        <li>
          <ListOption>REPOUSO RELATIVO NO LEITO À 30°</ListOption>
          <p className="error">
            PARA CADASTRAR UM ANTIBIÓTICO É NECESSÁRIO COLOCAR QUAL FOI O DIA
            INICIAL DE USO ESCREVENDO “D0 12/08/2022”
          </p>
        </li>
      </ol>
      <p className="legend">ÚLTIMA PRESCRIÇÃO ATUALIZADA EM DD/MM/AAAA HH:DD</p>
      <div className="buttons">
        <Button className="button_add_prescription">
          Adicionar medicações sintomáticas
        </Button>
        <Button className="button_normal">Adicionar nova linha</Button>
      </div>
      <Button className="button_normal button-update_prescription">
        Atualizar prescrição
      </Button>
    </div>
    <div className="pendencies_pacient">
      <h2>Pendências</h2>
      <TextArea placeholder="AQUI SEGUE UM TEXTO COM AS PENDÊNCIAS"></TextArea>
      <p className="legend">ÚLTIMA PENDÊNCIA ATUALIZADA EM DD/MM/AAAA HH:DD</p>
      <Button className="button_normal button-update_pendencies">
        Atualizar Pendências
      </Button>
    </div>
  </Container>
);

export default Evolution;
