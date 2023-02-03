import Container from "./styles";

import Button from "components/Button";
import { useLazyQuery } from "@apollo/client";
import { GET_ALL_CHART } from "graphql/queries";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import { useState } from "react";
import { format, parseISO } from "date-fns";
import ptBR from "date-fns/esm/locale/pt-BR";
import React from "react";
import Strategies from "./Strategies";
import updatePacientData from "helpers/updatePacientData";
import { useModalContext } from "services/ModalContext";

const Chart = () => {
  const [getInternment, { data }] = useLazyQuery(GET_ALL_CHART);
  const [newestChart, setNewestChart] = useState({
    prescriptions: [],
    sinals: {},
    textEvolution: "",
  });
  const [oldCharts, setOldCharts] = useState([]);
  const params = useParams();
  const { addModal } = useModalContext();

  const formatPrescription = (prescription) => {
    const array = [];

    if (prescription.diet?.name) {
      array.push({
        id: prescription.diet.name,
        value: prescription.diet.name,
      });
    }
    if (prescription.restingActivity?.name) {
      array.push({
        id: prescription.restingActivity.name,
        value: prescription.restingActivity.name,
      });
    }
    prescription.nursingActivities.forEach((nursingActivitie) => {
      array.push({
        id: nursingActivitie.name,
        value: nursingActivitie.name,
      });
    });
    prescription.drugPrescriptions.forEach((drug) => {
      array.push({
        id: drug.drug.name,
        value: `${drug.drug.name} ${drug.route}`,
      });
    });

    return array;
  };

  function templateFormatedData(data, handler) {
    return data.map((prescription, index) => {
      const handleFormated = handler
        ? handler(prescription, index)
        : prescription;
      const dateFormated = format(
        parseISO(prescription.createdAt),
        "dd/MM/yyyy HH:mm:ss",
        {
          locale: ptBR,
        }
      );
      return {
        ...handleFormated,
        dateFormated,
      };
    });
  }

  useEffect(() => {
    if (!data) {
      return;
    }
    const array = {
      prescriptions: [],
      sinals: {},
      textEvolution: "",
    };
    let oldChards = [];

    if (data.internment.prescriptions.length > 0) {
      const prescriptions = [...data.internment.prescriptions];
      const prescription = prescriptions.splice(
        data.internment.prescriptions.length - 1,
        1
      )[0];
      const prescriptionFormated = formatPrescription(prescription);
      array.prescriptions.push(...prescriptionFormated);
      const prescriptionsFormated = templateFormatedData(
        prescriptions,
        (prescription) => ({
          items: formatPrescription(prescription),
          __typename: prescription.__typename,
        })
      );

      oldChards = [...oldChards, ...prescriptionsFormated];
    }
    if (data.internment.measures.length > 0) {
      const measures = [...data.internment.measures];
      const fluidBalances = [...data.internment.fluidBalance];
      const measure = measures.splice(
        data.internment.measures.length - 1,
        1
      )[0];
      const fluidBalance = fluidBalances.splice(
        data.internment.measures.length - 1,
        1
      )[0];
      array.sinals = {
        cardiacFrequency: measure.cardiacFrequency,
        fetalCardiacFrequency: measure.fetalCardiacFrequency,
        celciusAxillaryTemperature: measure.celciusAxillaryTemperature,
        createdAt: measure.createdAt,
        diastolicBloodPressure: measure.diastolicBloodPressure,
        glucose: measure.glucose,
        pain: measure.pain,
        respiratoryFrequency: measure.respiratoryFrequency,
        spO2: measure.spO2,
        systolicBloodPressure: measure.systolicBloodPressure,
        volumeMl: fluidBalance.volumeMl,
        descriptionVolumeMl: fluidBalance.description.value,
      };
      const measuresWithDateFormat = templateFormatedData(
        measures,
        (measure, index) => {
          const fluidBalance = fluidBalances[index];
          return {
            ...measure,
            volumeMl: fluidBalance.volumeMl,
            descriptionVolumeMl: fluidBalance.description.value,
          };
        }
      );
      oldChards = [...oldChards, ...measuresWithDateFormat];
    }
    if (data.internment.evolutions.length > 0) {
      const evolutions = [...data.internment.evolutions];
      const evolution = evolutions.splice(
        data.internment.evolutions.length - 1,
        1
      )[0];
      array.textEvolution = evolution.text;
      const evolutionsWithDateFormat = templateFormatedData(evolutions);
      oldChards = [...oldChards, ...evolutionsWithDateFormat];
    }
    if (data.internment.pendings.length > 0) {
      const pendingsWithDateFormat = templateFormatedData(
        data.internment.pendings
      );
      oldChards = [...oldChards, ...pendingsWithDateFormat];
    }
    oldChards.sort((chartA, chartB) => {
      const dataChartA = new Date(chartA.createdAt);
      const dataChartB = new Date(chartB.createdAt);
      if (dataChartA.getTime() > dataChartB.getTime()) {
        return -1;
      }
      return 1;
    });
    setOldCharts(oldChards);
    setNewestChart(array);
  }, [data]);

  useEffect(() => {
    getInternment({
      variables: {
        internment: params.id,
      },
    });
  }, [params]);

  return (
    <Container>
      <div className="header">
        <h2>Evoluir Paciente (João Miguel dos Santos Polenta, 83 anos)</h2>
        <Button
          type="button"
          onClick={() => addModal(updatePacientData(params.id))}
        >
          Atualizar Dados do Paciente
        </Button>
      </div>
      <h2>Admissão</h2>
      <p>{newestChart.textEvolution}</p>
      <h2>Últimas 24h (17/07/2022 7h - 18/07/2022 7h)</h2>
      <p>{newestChart.textEvolution}</p>
      <h2 className="secondary">Prescrições</h2>
      <ol>
        {newestChart.prescriptions.map((prescription) => (
          <li key={prescription.id}>{prescription.value}</li>
        ))}
      </ol>
      <h2 className="secondary">Sinais Vitais</h2>
      <ul>
        <li>FC {newestChart.sinals?.cardiacFrequency}bpm </li>
        <li>FCF {newestChart.sinals?.fetalCardiacFrequency}bpm </li>
        <li>HGT 110 </li>
        <li>FR {newestChart.respiratoryFrequency} </li>
        <li>TEMP AXILAR {newestChart.celciusAxillaryTemperature} </li>
        <li>
          BALANÇO HÍDRICO <strong>TOTAL -500</strong> 110 - COPO COM ÁGUA
        </li>
      </ul>
      <h2>Demais Evoluções</h2>
      {oldCharts.map((oldChart) => (
        <div>
          <Strategies oldChart={oldChart} />
        </div>
      ))}
    </Container>
  );
};

export default Chart;
