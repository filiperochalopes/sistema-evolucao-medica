export const PendingStrategy = (value) => (
  <>
    <h2 className="secondary">Pendências {value.dateFormated}</h2>
    <p>{value.text}</p>
  </>
);

const MeasureStrategy = (value) => (
  <>
    <h2 className="secondary">Sinais Vitais {value.dateFormated}</h2>
    <ul>
      {value.cardiacFrequency !== null && (
        <li>FC {value.cardiacFrequency}bpm </li>
      )}
      {value.fetalCardiacFrequency !== null && (
        <li>FCF {value.fetalCardiacFrequency}bpm</li>
      )}
      {value.glucose !== null && <li>HGT {value.glucose} </li>}
      {value.respiratoryFrequency !== null && (
        <li>FR {value.respiratoryFrequency} </li>
      )}
      {value.celciusAxillaryTemperature !== null && (
        <li>TEMP AXILAR {value.celciusAxillaryTemperature}</li>
      )}
      {value.spO2 !== null && <li>Pressão Arterial {value.spO2}</li>}
      {value.pain !== null && <li>DOR {value.pain}</li>}
      {value.systolicBloodPressure !== null && (
        <li>PAS {value.systolicBloodPressure}</li>
      )}
      {value.diastolicBloodPressure !== null && (
        <li>PAD {value.diastolicBloodPressure}</li>
      )}
      {/* <li>
        BALANÇO HÍDRICO <strong>TOTAL -500</strong> 110 - COPO COM ÁGUA
      </li> */}
    </ul>
  </>
);

const EvolutionStrategy = (value) => (
  <>
    <h2 className="secondary">Evolução {value.dateFormated}</h2>
    <p>{value.text} </p>
  </>
);

export const PrescriptionStrategy = (value) => (
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
