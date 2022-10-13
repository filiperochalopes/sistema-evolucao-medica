import Container, { Inputs } from "./styles";

import Button from "components/Button";
import Input from "components/Input";

const VitalSign = () => (
  <Container>
    <h2>Adicionar Dados de Sinais vitais e Balanço Hídrico</h2>
    <div className="input">
      <p>FREQUENCIA CARDÍACA:</p>
      <Inputs>
        <div>
          <Input className="small" />
          <p>BPM</p>
        </div>
      </Inputs>
    </div>
    <div className="input">
      <p>FREQUENCIA CARDÍACA:</p>
      <Inputs>
        <div>
          <Input className="small" />
          <p>BPM</p>
        </div>
      </Inputs>
    </div>
    <div className="input">
      <p>FREQUÊNCIA RESPIRATÓRIA:</p>
      <Inputs>
        <div>
          <Input className="small" />
          <p>IPM</p>
        </div>
      </Inputs>
    </div>
    <div className="input">
      <p>DOR (ESCALA DE 1 A 10):</p>
      <Inputs>
        <Input className="small" />
        <Input placeholder="LOCALIZAÇÃO DA DOR" />
      </Inputs>
    </div>
    <div className="input">
      <p>TEMPERATURA AXILAR:</p>
      <Inputs>
        <Input className="small" />
      </Inputs>
    </div>
    <div className="input">
      <p>PRESSÃO ARTERIAL:</p>
      <Inputs>
        <Input className="small" />
      </Inputs>
    </div>
    <div className="input">
      <p>DADO DE BALANÇO HÍDRICO:</p>
      <Inputs>
        <div>
          <Input className="small" />
          <p>ML</p>
        </div>
        <Input placeholder="DESCRIÇÃO" />
      </Inputs>
    </div>
    <div className="input">
      <p>GLICEMIA PERIFÉRICA:</p>
      <Inputs>
        <Input className="small" />
      </Inputs>
    </div>
    <Button>Adicionar Sinais Vitais</Button>
  </Container>
);

export default VitalSign;
