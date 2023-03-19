/* eslint-disable react-hooks/rules-of-hooks */
import { useQuery } from "@apollo/client";
import Button from "components/Button";
import { DRUG_PRESETS } from "graphql/queries";
import { useEffect, useState } from "react";
import Container, { GroupMedicament } from "./styles";

const ModalMedicamentGroup = ({ confirmButton, currentMedicament }) => {
  const { data } = useQuery(DRUG_PRESETS);
  const [presets, setPresets] = useState();

  useEffect(() => {
    if (!data) {
      return;
    }
    const newPresets = data.drugPresets.map((drugPreset) => {
      const drugText = drugPreset.drugs.reduce(
        (drug, current, index) =>
          drug +
          `Medicação ${index + 1},${current.name} ${current.usualDosage}+ ";"`,
        ""
      );
      return {
        ...drugPreset,
        drugText,
      };
    });
    setPresets({ drugPresets: newPresets });
  }, [data]);

  return (
    <Container>
      {presets &&
        presets?.drugPresets.map((drugPreset, index) => (
          <GroupMedicament
            selected={drugPreset.active}
            onClick={() => {
              const setNewGroups = presets.drugPresets.map(
                (drug, indexDrug) => {
                  const { active, ...rest } = drug;
                  if (indexDrug === index && !active) {
                    return { ...rest, active: true };
                  }
                  return rest;
                }
              );
              setPresets({ drugPresets: setNewGroups });
            }}
            type="button"
            key={drugPreset.label}
            className="group"
          >
            <h2>{drugPreset.label}</h2>
            <p>{drugPreset.drugText}</p>
          </GroupMedicament>
        ))}
      <Button
        className="add_button"
        type="button"
        onClick={() => {
          const filterMedicaments = [];
          presets?.drugPresets.forEach((drug) => {
            if (!drug.active) {
              return;
            }
            drug.drugs.forEach((drug) => {
              const findCurrentDrug = currentMedicament.find(
                (medicament) =>
                  medicament.drugName === drug.name &&
                  drug.usualRoute === medicament.route
              );
              if (findCurrentDrug) {
                return;
              }
              filterMedicaments.push({
                block: true,
                id: drug.id,
                drugName: drug.name,
                drugKind: drug.kind,
                dosage: drug.usualDosage,
                route: drug.usualRoute,
                initialDate: undefined,
                endingDate: undefined,
              });
            });
          });
          confirmButton(filterMedicaments);
        }}
      >
        Adicionar Linha
      </Button>
    </Container>
  );
};

export default ModalMedicamentGroup;
