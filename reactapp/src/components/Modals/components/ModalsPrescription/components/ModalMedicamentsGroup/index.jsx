/* eslint-disable react-hooks/rules-of-hooks */
import { useQuery } from "@apollo/client";
import Button from "components/Button";
import { DRUG_PRESETS } from "graphql/queries";
import { useEffect, useState } from "react";
import Container from "./styles";
import PrescriptionGroupInput from "components/Modals/components/PrescriptionGroupInput";

const ModalMedicamentGroup = ({ confirmButton, currentMedicament }) => {
  const { data: drugPresetsData } = useQuery(DRUG_PRESETS);
  const [presets, setPresets] = useState([]);
  const [selectedPreset, setSelectedPreset] = useState(null);

  useEffect(() => {
    console.log(drugPresetsData);
    if (!drugPresetsData) {
      return;
    }
    const _presets = drugPresetsData.drugPresets.map((drugPreset) => {
      const description = drugPreset.drugs.reduce(
        (acc, cur, index) =>
          acc + `${index + 1}. ${cur.name} ${cur.usualDosage}\n`,
        ""
      );
      return {
        ...drugPreset,
        description,
      };
    });
    console.log(_presets);
    setPresets(_presets);
  }, [drugPresetsData]);

  return (
    <Container>
      {presets.length &&
        presets?.map((drugPreset) => (
          <PrescriptionGroupInput
            optionId={drugPreset.id}
            name="preset"
            id={drugPreset.name}
            onChange={() => setSelectedPreset(drugPreset)}
            description={
              <div>
                <h2>{drugPreset.label}</h2>
                <p>{drugPreset.description}</p>
              </div>
            }
          />
        ))}
      <Button
        className="add_button"
        type="button"
        onClick={() => {
          const drugPrescriptions = [];
          selectedPreset.drugs.forEach((drug) => {
            drugPrescriptions.push({
              block: true,
              id: drug.id,
              drugName: drug.name,
              drugKind: drug.kind,
              dosage: drug.usualDosage,
              route: drug.usualRoute,
              initialDate: undefined,
              endingDate: undefined,
            });
            console.log(drugPrescriptions);
          });
          confirmButton(drugPrescriptions);
        }}
      >
        Adicionar Linha
      </Button>
    </Container>
  );
};

export default ModalMedicamentGroup;
