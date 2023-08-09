import Container from "./styles";

import Button from "components/Button";
import { useLazyQuery, useMutation } from "@apollo/client";
import { GET_ALL_CHART } from "graphql/queries";
import { Link, useParams } from "react-router-dom";
import { useEffect } from "react";
import { useState } from "react";
import { format, intervalToDuration, parseISO } from "date-fns";
import ptBR from "date-fns/locale/pt-BR";
import React from "react";
import Strategies, {
  PendingStrategy,
  PrescriptionStrategy,
} from "./Strategies";
import updatePacientData from "helpers/updatePacientData";
import { useModalContext } from "services/ModalContext";
import { GENERATE_PDF_BALANCO_HIDRICO } from "graphql/mutations";
import b64toBlob from "utils/b64toBlob";
import CheckRole from "routes/CheckRole";
import useHandleErrors from "hooks/useHandleErrors";
import verifyIfDateIsRangeCurrentDate from "utils/verifyIfDateIsRangeCurrentDate";
import { useCallback } from "react";

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
  spO2: {
    title: "Pressão Arterial",
    legend: "",
  },
  pain: {
    title: "DOR",
    legend: "",
  },
  systolicBloodPressure: {
    title: "PAS",
    legend: "",
  },
  diastolicBloodPressure: {
    title: "PAD",
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
    pending: [],
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

  const handlePrescriptions = useCallback((currentPrescriptions) => {
    const prescriptions = [];
    const oldPrescriptions = [];

    const verifyDate = verifyIfDateIsRangeCurrentDate();
    if (currentPrescriptions.length > 0) {
      currentPrescriptions.forEach((currentPrescription) => {
        const prescription = formatPrescription(currentPrescription);
        const dateFormated = format(
          parseISO(currentPrescription.createdAt),
          "dd/MM/yyyy HH:mm:ss",
          {
            locale: ptBR,
          }
        );
        try {
          verifyDate.verifyDate(new Date(currentPrescription.createdAt));
          prescriptions.push({
            items: prescription,
            dateFormated,
          });
        } catch (e) {
          oldPrescriptions.push({
            items: prescription,
            dateFormated,
            __typename: currentPrescription.__typename,
          });
        }
      });
    }

    return { prescriptions, oldPrescriptions };
  }, []);

  const handleMeasures = useCallback((currentMeasures) => {
    const sinals = {};
    const oldMeasures = [];

    const verifyDate = verifyIfDateIsRangeCurrentDate();
    currentMeasures.forEach((measure) => {
      try {
        verifyDate.verifyDate(new Date(measure.createdAt));
        const keysMeasure = Object.keys(measure);
        keysMeasure.forEach((key) => {
          if (typeof measure[key] !== "number") {
            return;
          }
          if (!sinals[key]) {
            sinals[key] = {
              title: `${MEASURES_TITLES[key]?.title} ` || " ",
              array: [],
            };
          }
          sinals[key].array.push({
            text: `${measure[key]}  ` + (MEASURES_TITLES[key]?.legend || ""),
            date: format(parseISO(measure.createdAt), "HH:mm:ss", {
              locale: ptBR,
            }),
            id: sinals[key].array.length,
          });
        });
      } catch (e) {
        oldMeasures.push(measure);
      }
    });

    return { sinals, oldMeasures };
  }, []);

  const handleFluids = useCallback(
    (currentFluids) => {
      const verifyDate = verifyIfDateIsRangeCurrentDate();
      let total = 0;
      const fluids = [];
      let newFluids = {};
      currentFluids.forEach((fluidBalance) => {
        try {
          verifyDate.verifyDate(new Date(fluidBalance.createdAt));
          total += fluidBalance?.volumeMl || 0;
          fluids.push({
            volumeMl: fluidBalance?.volumeMl || 0,
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
        newFluids = {
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
      return { fluids: newFluids };
    },

    // eslint-disable-next-line react-hooks/exhaustive-deps
    [params.id, printFluids]
  );

  const handleEvolutions = useCallback((currentEvolutions) => {
    const verifyDate = verifyIfDateIsRangeCurrentDate();
    const evolutionsText = [];
    const othersEvolutions = [];
    if (currentEvolutions.length > 0) {
      const date = new Date();
      currentEvolutions.forEach((currentEvolution) => {
        try {
          verifyDate.verifyDate(new Date(currentEvolution.createdAt));
          const response = intervalToDuration({
            start: parseISO(currentEvolution.createdAt),
            end: date,
          });
          if (response.days <= 2) {
            evolutionsText.push(currentEvolution);
          } else {
            othersEvolutions.push(currentEvolution);
          }
        } catch {
          console.log("error");
          const dateFormated = format(
            parseISO(currentEvolution.createdAt),
            "dd/MM/yyyy HH:mm:ss",
            {
              locale: ptBR,
            }
          );
          othersEvolutions.push({
            ...currentEvolution,
            dateFormated,
          });
        }
      });
    }
    return { evolutionsText, othersEvolutions };
  }, []);

  const handlePendents = useCallback((currentPendents) => {
    const verifyDate = verifyIfDateIsRangeCurrentDate();
    const pendents = [];
    const oldPendents = [];
    if (currentPendents.length > 0) {
      currentPendents.forEach((currentPendent) => {
        try {
          verifyDate.verifyDate(new Date(currentPendent.createdAt));

          pendents.push(currentPendent);
        } catch {
          const dateFormated = format(
            parseISO(currentPendent.createdAt),
            "dd/MM/yyyy HH:mm:ss",
            {
              locale: ptBR,
            }
          );
          oldPendents.push({
            ...currentPendent,
            dateFormated,
          });
        }
      });
    }
    return { oldPendents, pendents };
  }, []);

  useEffect(() => {
    if (!data) {
      return;
    }
    const array = {
      prescriptions: [],
      sinals: {},
      textEvolution: [],
      pending: [],
    };
    let oldChards = [];
    const prescriptions = handlePrescriptions(data.internment.prescriptions);

    oldChards = [...oldChards, ...prescriptions.oldPrescriptions];
    array.prescriptions.push(...prescriptions.prescriptions);

    const oldMeasures = [];
    const measures = handleMeasures(data.internment.measures);
    array.sinals = measures.sinals;
    oldMeasures.push(...measures.oldMeasures);
    oldChards = [...oldChards, ...measures.oldMeasures];

    const fluids = handleFluids(data.internment.fluidBalance);

    array.sinals.fluids = fluids.fluids;
    const measuresWithDateFormat = templateFormatedData(
      oldMeasures,
      (measure, index) => {
        const fluidBalance = data.internment.fluidBalance[index];
        return {
          ...measure,
          volumeMl: fluidBalance?.volumeMl,
          descriptionVolumeMl: fluidBalance?.description?.value,
        };
      }
    );

    oldChards = [...oldChards, ...measuresWithDateFormat];
    const evolutions = handleEvolutions(data.internment.evolutions);
    array.textEvolution = evolutions.evolutionsText;
    oldChards = [...oldChards, ...evolutions.othersEvolutions];
    const pendents = handlePendents(data.internment.pendings);

    array.pending = pendents?.pendents || [];
    oldChards = [...oldChards, ...pendents.oldPendents];

    oldChards.sort((chartA, chartB) => {
      const dataChartA = new Date(chartA.createdAt);
      const dataChartB = new Date(chartB.createdAt);
      if (dataChartA.getTime() > dataChartB.getTime()) {
        return -1;
      }
      return 1;
    });
    console.log("array", array);
    setOldCharts(oldChards);
    setNewestChart(array);
  }, [
    data,
    handleEvolutions,
    handleFluids,
    handleMeasures,
    handlePendents,
    handlePrescriptions,
  ]);

  useEffect(() => {
    getInternment({
      variables: {
        internment: params.id,
      },
    });
  }, [getInternment, params]);
  console.log("newestChart", newestChart);

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
            onClick={() => {
              addModal(updatePacientData(data.internment.patient.id));
            }}
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
      {newestChart.prescriptions.map((prescription) => (
        <PrescriptionStrategy {...prescription} />
      ))}
      <h2>Sinais Vitais</h2>
      <ul>
        {Object.keys(newestChart.sinals).map((key) => (
          <li>
            {newestChart?.sinals[key].title}
            {newestChart?.sinals[key]?.array?.map((text) =>
              typeof text.text === "string"
                ? text.text + " " + text.date + " "
                : text.text
            )}
          </li>
        ))}
      </ul>
      {newestChart.pending.length > 0 &&
        newestChart.pending.map((pending) => (
          <PendingStrategy
            dateFormated={pending?.dateFormated}
            text={pending?.text}
          />
        ))}

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
