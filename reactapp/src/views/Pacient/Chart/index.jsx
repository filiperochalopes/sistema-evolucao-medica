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
import useHandleErrors from "hooks/useHandleErrors";
import verifyIfDateIsRangeCurrentDate from "utils/verifyIfDateIsRangeCurrentDate";

const MEASURES_TITLES = {
  cardiacFrequency: {
    title: "FC",
    legend: "bpm",
  },
  fetalCardiacFrequency: {
    title: "FCF",
    legend: "bpm",
  },
  glucose: {
    title: "HGT",
    legend: "mg/ml",
  },
  respiratoryFrequency: {
    title: "FR",
    legend: "",
  },
  celciusAxillaryTemperature: {
    title: "TEMP AXILAR",
    legend: "",
  },
};

const Chart = () => {
  const [getInternment, { data }] = useLazyQuery(GET_ALL_CHART, {
    fetchPolicy: "no-cache",
  });
  const { handleErrors } = useHandleErrors();
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
        value: `${drug.drug.name} ${drug.route} ${drug.dosage} ${initialDate} ${finalDate}`,
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
    const verifyDate = verifyIfDateIsRangeCurrentDate();
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
    const oldMeasures = [];
    data.internment.measures.forEach((measure) => {
      try {
        verifyDate.verifyDate(new Date(measure.createdAt));
        const keysMeasure = Object.keys(measure);
        keysMeasure.forEach((key) => {
          if (typeof measure[key] !== "number") {
            return;
          }
          if (!array.sinals[key]) {
            array.sinals[key] = {
              title: MEASURES_TITLES[key].title,
              array: [],
            };
          }
          array.sinals[key].array.push({
            text: `${measure[key]}` + MEASURES_TITLES[key].legend,
            date: format(parseISO(measure.createdAt), "HH:mm:ss", {
              locale: ptBR,
            }),
            id: array.sinals[key].array.length,
          });
        });
      } catch {
        oldMeasures.push(measure);
      }
    });

    let total = 0;
    const fluids = [];
    data.internment.fluidBalance.forEach((fluidBalance) => {
      try {
        verifyDate.verifyDate(new Date(fluidBalance.createdAt));
        total += fluidBalance.volumeMl;
        fluids.push({
          volumeMl: fluidBalance.volumeMl,
          descriptionVolumeMl: fluidBalance.description.value,
        });
      } catch (e) {
        console.log("error fluid");
      }
    });
    if (fluids.length > 0) {
      const text = fluids.reduce(
        (oldText, fluid) =>
          oldText + ` ${fluid.volumeMl}ml - ${fluid.descriptionVolumeMl}`,
        ""
      );
      array.sinals.fluids = {
        title: (
          <>
            Balanço Hídrico <strong>Total {total}</strong>
          </>
        ),
        array: [
          {
            text: (
              <>
                {text}{" "}
                <button
                  type="button"
                  onClick={async () => {
                    try {
                      let initialDate = new Date();
                      let endDate = new Date();

                      if (initialDate.getHours() > 7) {
                        endDate.setDate(initialDate.getDate() + 1);
                      } else {
                        initialDate.setDate(initialDate.getDate() - 1);
                      }
                      initialDate = format(initialDate, "yyyy/MM/dd", {
                        locale: ptBR,
                      });
                      endDate = format(endDate, "yyyy/MM/dd", {
                        locale: ptBR,
                      });

                      const response = await printFluids({
                        variables: {
                          internmentId: Number(params.id),
                          extra: {
                            interval: {
                              startDatetimeStamp: `${initialDate}:07:00`,
                              endingDatetimeStamp: `${endDate}:07:00`,
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
                    } catch (e) {
                      handleErrors(e);
                    }
                  }}
                >
                  para ter uma visão geral do balanço hídrico acesse esse link
                </button>
              </>
            ),
            date: "",
            id: 1,
          },
        ],
      };
    }
    const measuresWithDateFormat = templateFormatedData(
      oldMeasures,
      (measure, index) => {
        const fluidBalance = data.internment.fluidBalance[index];
        return {
          ...measure,
          volumeMl: fluidBalance.volumeMl,
          descriptionVolumeMl: fluidBalance.description.value,
        };
      }
    );

    oldChards = [...oldChards, ...measuresWithDateFormat];
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
      {data?.internment?.hpi && (
        <>
          <h2>Admissão</h2>
          <p>{data?.internment?.hpi}</p>
        </>
      )}
      {newestChart.textEvolution.length > 0 && (
        <>
          <h2>Últimas Atualizações</h2>
          {newestChart.textEvolution.map((evolution) => (
            <p>{evolution?.text}</p>
          ))}
        </>
      )}
      {newestChart.prescriptions.length > 0 && (
        <h2 className="secondary">Prescrições</h2>
      )}
      <ol>
        {newestChart.prescriptions.map((prescription) => (
          <li key={prescription.id}>{prescription.value}</li>
        ))}
      </ol>
      <h2>Sinais Vitais</h2>
      <ul>
        {Object.keys(newestChart.sinals).map((key) => (
          <li>
            {newestChart.sinals[key].title}
            {newestChart.sinals[key].array.map((text) =>
              typeof text.text === "string"
                ? text.text + " " + text.date + " "
                : text.text
            )}
          </li>
        ))}
      </ul>
      {newestChart.pending?.text && (
        <PendingStrategy
          dateFormated={newestChart.pending?.dateFormated}
          text={newestChart.pending?.text}
        />
      )}
      {oldCharts.length > 0 && (
        <>
          <h2>Demais Evoluções</h2>
          {oldCharts.map((oldChart) => (
            <div>
              <Strategies oldChart={oldChart} />
            </div>
          ))}
        </>
      )}
    </Container>
  );
};

export default Chart;
