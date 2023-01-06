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

  useEffect(() => {
    if (!data) {
      return;
    }
    const array = {
      prescriptions: [],
      sinals: [],
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
      const prescriptionsFormated = [];
      prescriptions.forEach((prescription) => {
        const prescriptionFormated = formatPrescription(prescription);
        const dateFormated = format(
          parseISO(prescription.createdAt),
          "dd/MM/yyyy HH:mm:ss",
          {
            locale: ptBR,
          }
        );
        prescriptionsFormated.push({
          items: prescriptionFormated,
          createdAt: prescription.createdAt,
          dateFormated,
          __typename: prescription.__typename,
        });
      });
      oldChards = [...oldChards, ...prescriptionsFormated];
    }
    if (data.internment.measures.length > 0) {
      const measures = [...data.internment.measures];
      const measure = measures.splice(
        data.internment.measures.length - 1,
        1
      )[0];
      const measuresWithDateFormat = measures.map((measure) => {
        const dateFormated = format(
          parseISO(measure.createdAt),
          "dd/MM/yyyy HH:mm:ss",
          {
            locale: ptBR,
          }
        );
        return { ...measure, dateFormated };
      });

      oldChards = [...oldChards, ...measuresWithDateFormat];
    }
    if (data.internment.evolutions.length > 0) {
      const evolutions = [...data.internment.evolutions];
      const evolution = evolutions.splice(
        data.internment.evolutions.length - 1,
        1
      )[0];
      array.textEvolution = evolution.text;
      const evolutionsWithDateFormat = evolutions.map((evolution) => {
        const dateFormated = format(
          parseISO(evolution.createdAt),
          "dd/MM/yyyy HH:mm:ss",
          {
            locale: ptBR,
          }
        );
        return { ...evolution, dateFormated };
      });

      oldChards = [...oldChards, ...evolutionsWithDateFormat];
    }
    if (data.internment.pendings.length > 0) {
      const pendingsWithDateFormat = data.internment.pendings.map((pending) => {
        const dateFormated = format(
          parseISO(pending.createdAt),
          "dd/MM/yyyy HH:mm:ss",
          {
            locale: ptBR,
          }
        );
        return { ...pending, dateFormated };
      });

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
    console.log(oldChards);
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
      {oldCharts.map((oldChart) => (
        <div>
          <Strategies oldChart={oldChart} />
        </div>
      ))}
    </Container>
  );
};

export default Chart;
