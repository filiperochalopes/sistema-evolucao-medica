import Container from "./styles";

import Button from "components/Button";

const Chart = () => (
  <Container>
    <div className="header">
      <h2>Evoluir Paciente (João Miguel dos Santos Polenta, 83 anos)</h2>
      <Button>Atualizar Dados do Paciente</Button>
    </div>
    <h2>Admissão</h2>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. In lectus erat,
      cursus id arcu quis, imperdiet feugiat dui. Integer rutrum, turpis non
      semper feugiat, diam est ornare nisi, sit amet lobortis ipsum turpis ac
      arcu. Praesent ut velit elit. Sed justo libero, gravida id porta ut,
      facilisis a leo. In tristique, dui sed dignissim vehicula, nisl orci
      aliquam velit, nec condimentum eros nunc sollicitudin risus. Sed
      vestibulum ipsum ut sem vehicula aliquam. Aenean at nunc aliquet, feugiat
      dolor vel, consectetur elit. Integer auctor est eget scelerisque finibus.
      Vestibulum iaculis scelerisque enim. Sed consectetur nibh at tristique
      sagittis. Quisque ac tincidunt augue. Nam iaculis neque leo, vel suscipit
      nulla varius quis. Mauris rhoncus, sem sed eleifend rutrum, dui risus
      porttitor lorem, ut tristique erat lacus a quam.
    </p>
    <h2>Últimas 24h (17/07/2022 7h - 18/07/2022 7h)</h2>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. In lectus erat,
      cursus id arcu quis, imperdiet feugiat dui. Integer rutrum, turpis non
      semper feugiat, diam est ornare nisi, sit amet lobortis ipsum turpis ac
      arcu. Praesent ut velit elit. Sed justo libero, gravida id porta ut,
      facilisis a leo. In tristique, dui sed dignissim vehicula, nisl orci
      aliquam velit, nec condimentum eros nunc sollicitudin risus. Sed
      vestibulum ipsum ut sem vehicula aliquam. Aenean at nunc aliquet, feugiat
      dolor vel, consectetur elit. Integer auctor est eget scelerisque finibus.
      Vestibulum iaculis scelerisque enim.
    </p>
    <h2 className="secondary">Prescrições</h2>
    <ol>
      <li>Repouso relativo</li>
      <li>Dieta zero</li>
      <li>Dipirona 1g 6/6h Se dor ou temperatura maior do que 37,8°C</li>
      <li>Ibuprofeno 600mg 8/8h</li>
      <li>Praesent ut velit elit.</li>
      <li>Praesent ut velit elit.</li>
      <li>Praesent ut velit elit.</li>
    </ol>
    <h2 className="secondary">Sinais Vitais</h2>
    <ul>
      <li>FC 50bpm (17/07/2022 5:30) 60bpm (17/07/2022 8:30)</li>
      <li>HGT 110 (17/07/2022 5:30)</li>
      <li>FR 110 (17/07/2022 5:30)</li>
      <li>TEMP AXILAR 110 (17/07/2022 5:30)</li>
      <li>
        BALANÇO HÍDRICO <strong>TOTAL -500</strong> 110 - COPO COM ÁGUA
        (17/07/2022 5:30)
      </li>
    </ul>
    <h2>Demais Evoluções</h2>
  </Container>
);

export default Chart;
