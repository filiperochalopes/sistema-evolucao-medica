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
import Strategies, { PendingStrategy } from "./Strategies";
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
    textEvolution: [],
    pending: {},
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
      textEvolution: [],
      pending: {},
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
      const object = {
        cardiacFrequency: "",
        cardiacFrequencyCreatedAt: "",
        fetalCardiacFrequency: "",
        fetalCardiacFrequencyCreatedAt: "",
        celciusAxillaryTemperature: "",
        celciusAxillaryTemperatureCreatedAt: "",
        createdAt: "",
        diastolicBloodPressure: "",
        diastolicBloodPressureCreatedAt: "",
        glucose: "",
        glucoseCreatedAt: "",
        pain: "",
        painCreatedAt: "",
        respiratoryFrequency: "",
        respiratoryFrequencyCreatedAt: "",
        spO2: "",
        spO2CreatedAt: "",
        systolicBloodPressure: "",
        systolicBloodPressureCreatedAt: "",
        fluids: [],
        totalFluids: "",
      };
      console.log(measures[0]);
      // eslint-disable-next-line for-direction
      for (let i = measures.length - 1; i > 0; i--) {
        console.log("Oi");
        const objectKeys = Object.keys(measures[i]);
        objectKeys.forEach((key) => {
          if (!object[key] && measures[i][key]) {
            object[key] = measures[i][key];
            object[`${key}CreatedAt`] = format(
              parseISO(measures[i].createdAt),
              "dd/MM/yyyy HH:mm:ss",
              {
                locale: ptBR,
              }
            );
          }
        });
      }

      let total = 0;
      const fluids = [];
      const date = new Date();
      fluidBalances.forEach((fluidBalance) => {
        if (object?.createdAt) {
          const response = intervalToDuration({
            start: parseISO(object.createdAt),
            end: date,
          });
          if (response.days <= 1) {
            total += fluidBalance.volumeMl;
            fluids.push({
              volumeMl: fluidBalance.volumeMl,
              descriptionVolumeMl: fluidBalance.description.value,
            });
          }
        } else {
          total += fluidBalance.volumeMl;
          fluids.push({
            volumeMl: fluidBalance.volumeMl,
            descriptionVolumeMl: fluidBalance.description.value,
          });
        }
      });
      object.fluids = fluids;
      object.totalFluids = total;
      array.sinals = object;
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
      const evolutionsText = [];
      const othersEvolutions = [];
      const date = new Date();
      for (let i = data.internment.evolutions.length - 1; i >= 0; i--) {
        const evolution = data.internment.evolutions[i];
        const response = intervalToDuration({
          start: parseISO(evolution.createdAt),
          end: date,
        });
        if (response.days <= 2) {
          evolutionsText.push(evolution);
        } else {
          othersEvolutions.push(evolution);
        }
      }
      const evolutions = [...othersEvolutions];
      array.textEvolution = evolutionsText;
      const evolutionsWithDateFormat = templateFormatedData(evolutions);
      oldChards = [...oldChards, ...evolutionsWithDateFormat];
    }

    if (data.internment.pendings.length > 0) {
      const pendings = [...data.internment.pendings];
      const pending = pendings.splice(
        data.internment.pendings.length - 1,
        1
      )[0];
      array.pending = templateFormatedData([pending])[0];
      const pendingsWithDateFormat = templateFormatedData(pendings);
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
  console.log(newestChart);
  return (
    <Container>
      <div className="header">
        <h2>
          <Link to={`/evoluir-paciente/${params.id}`}>Evoluir Paciente</Link> (
          {data?.internment?.patient?.name},{data?.internment?.patient?.age})
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
      <p>{data?.internment?.hpi}</p>
      <h2>Últimas Atualizações</h2>
      {newestChart.textEvolution.map((evolution) => (
        <p>{evolution?.text}</p>
      ))}
      <h2 className="secondary">Prescrições</h2>
      <ol>
        {newestChart.prescriptions.map((prescription) => (
          <li key={prescription.id}>{prescription.value}</li>
        ))}
      </ol>
      <h2 className="secondary">Sinais Vitais</h2>
      <ul>
        {newestChart.sinals?.cardiacFrequency && (
          <li>
            FC {newestChart.sinals?.cardiacFrequency}bpm{" "}
            {newestChart.sinals?.cardiacFrequencyCreatedAt}
          </li>
        )}
        {newestChart.sinals?.fetalCardiacFrequency && (
          <li>
            FCF {newestChart.sinals?.fetalCardiacFrequency}bpm{" "}
            {newestChart.sinals?.fetalCardiacFrequencyCreatedAt}{" "}
          </li>
        )}
        {newestChart.sinals?.glucose && (
          <li>
            HGT {newestChart.sinals?.glucose} mg/ml{" "}
            {newestChart.sinals?.glucoseCreatedAt}
          </li>
        )}
        {newestChart.sinals?.respiratoryFrequency && (
          <li>
            FR {newestChart.sinals?.respiratoryFrequency}{" "}
            {newestChart.sinals?.respiratoryFrequencyCreatedAt}
          </li>
        )}
        {newestChart.sinals?.celciusAxillaryTemperature && (
          <li>
            TEMP AXILAR {newestChart.sinals?.celciusAxillaryTemperature}{" "}
            {newestChart.sinals?.celciusAxillaryTemperatureCreatedAt}
          </li>
        )}
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
      <PendingStrategy
        dateFormated={newestChart.pending?.dateFormated}
        text={newestChart.pending?.text}
      />
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
