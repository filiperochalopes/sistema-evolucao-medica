const PendingStrategy = (value) => (
  <>
    <h2 className="secondary">Pendências {value.dateFormated}</h2>
    <p>{value.text}</p>
  </>
);

const MeasureStrategy = (value) => (
  <>
    <h2 className="secondary">Sinais Vitais {value.dateFormated}</h2>
    <ul>
      <li>FC {value.cardiacFrequency}bpm </li>
      <li>FCF {value.fetalCardiacFrequency}bpm</li>
      <li>HGT 110 </li>
      <li>FR {value.respiratoryFrequency} </li>
      <li>TEMP AXILAR {value.celciusAxillaryTemperature}</li>
      <li>
        BALANÇO HÍDRICO <strong>TOTAL -500</strong> 110 - COPO COM ÁGUA
      </li>
    </ul>
  </>
);

const EvolutionStrategy = (value) => (
  <>
    <h2 className="secondary">Evolução {value.dateFormated}</h2>
    <p>{value.text} </p>
  </>
);

const PrescriptionStrategy = (value) => (
  <>
    <h2 className="secondary">Prescrições {value.dateFormated}</h2>
    <ol>
      {value.items.map((item) => (
        <li key={item.id}>{item.value}</li>
      ))}
    </ol>
  </>
);

const StrategiesObject = {
  Prescription: PrescriptionStrategy,
  Evolution: EvolutionStrategy,
  Measure: MeasureStrategy,
  Pending: PendingStrategy,
};

const Strategies = ({ oldChart }) => {
  const Component = StrategiesObject[oldChart.__typename] || <></>;

  return <Component {...oldChart} />;
};

export default Strategies;
