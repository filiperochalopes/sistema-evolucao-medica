import Container from "./styles";

import Button from "components/Button";
import { useLazyQuery, useMutation } from "@apollo/client";
import { GET_ALL_CHART } from "graphql/queries";
import { Link, useParams } from "react-router-dom";
import { useEffect } from "react";
import { useState } from "react";
import { format, intervalToDuration, parseISO } from "date-fns";
import ptBR from "date-fns/esm/locale/pt-BR";
import React from "react";
import Strategies from "./Strategies";
import updatePacientData from "helpers/updatePacientData";
import { useModalContext } from "services/ModalContext";
import { GENERATE_PDF_BALANCO_HIDRICO } from "graphql/mutations";
import b64toBlob from "utils/b64toBlob";
import CheckRole from "routes/CheckRole";

const Chart = () => {
  const [getInternment, { data }] = useLazyQuery(GET_ALL_CHART);
  const [printFluids] = useMutation(GENERATE_PDF_BALANCO_HIDRICO);
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
      let initialDate = "";
      let finalDate = "";
      if (drug.initialDate) {
        initialDate = format(
          parseISO(drug.initialDate),
          "dd/MM/yyyy HH:mm:ss",
          {
            locale: ptBR,
          }
        );
        finalDate = format(parseISO(drug.endingDate), "dd/MM/yyyy HH:mm:ss", {
          locale: ptBR,
        });
      }
      array.push({
        id: drug.drug.name,
        value: `${drug.drug.name} ${drug.route} ${drug.dosage} ${drug.drug.name} ${initialDate} ${finalDate}`,
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
      let total = 0;
      const fluids = [];
      const date = new Date();
      fluidBalances.forEach((fluidBalance) => {
        const response = intervalToDuration({
          start: parseISO(measure.createdAt),
          end: date,
        });
        if (response.days <= 1) {
          total += fluidBalance.volumeMl;
          fluids.push({
            volumeMl: fluidBalance.volumeMl,
            descriptionVolumeMl: fluidBalance.description.value,
          });
        }
      });

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
        fluids: fluids,
        totalFluids: total,
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
  }, [getInternment, params]);

  return (
    <Container>
      <div className="header">
        <h2>
          <Link to={`/evoluir-paciente/${params.id}`}>Evoluir Paciente</Link> (
          {data?.internment?.patient?.name},{data?.internment?.patient?.age}{" "}
          anos)
        </h2>
        <CheckRole roles={["doc"]}>
          <Button
            type="button"
            onClick={() => addModal(updatePacientData(params.id))}
          >
            Atualizar Dados do Paciente
          </Button>
        </CheckRole>
      </div>
      <h2>Admissão</h2>
      <p>{newestChart.textEvolution}</p>
      <h2>Últimas Atualizações</h2>
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
        <li>HGT {newestChart.sinals?.glucose} mg/ml</li>
        <li>FR {newestChart.sinals?.respiratoryFrequency} </li>
        <li>TEMP AXILAR {newestChart.sinals?.celciusAxillaryTemperature} </li>
        <li>
          BALANÇO HÍDRICO{" "}
          <strong>TOTAL {newestChart.sinals?.totalFluids}</strong> |
          {(newestChart.sinals?.fluids || []).map(
            (fluid) => `${fluid.volumeMl}ml - ${fluid.descriptionVolumeMl}`
          )}
          <button
            type="button"
            onClick={async () => {
              const date = format(
                new Date(newestChart.sinals.createdAt),
                "yyyy/MM/dd",
                {
                  locale: ptBR,
                }
              );
              const response = await printFluids({
                variables: {
                  internmentId: Number(params.id),
                  extra: {
                    interval: {
                      startDatetimeStamp: `${date}:00:00`,
                      endingDatetimeStamp: `${date}:23:59`,
                    },
                  },
                },
              });
              const link = document.createElement("a");
              const file = b64toBlob(
                response.data.printPdf_BalancoHidrico.base64Pdf,
                "application/pdf"
              );
              const url = URL.createObjectURL(file);
              link.href = url;
              link.setAttribute("target", "_blank");
              link.click();
            }}
          >
            para ter uma visão geral do balanço hídrico acesse esse link
          </button>
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
