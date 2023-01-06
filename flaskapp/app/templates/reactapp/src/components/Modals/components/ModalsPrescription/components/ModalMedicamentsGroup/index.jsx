/* eslint-disable react-hooks/rules-of-hooks */
import { useQuery } from "@apollo/client";
import Button from "components/Button";
import { DRUG_PRESETS } from "graphql/queries";
import { useEffect, useState } from "react";
import Container, { GroupMedicament } from "./styles";

const ModalMedicamentGroup = ({ confirmButton }) => {
  const { data } = useQuery(DRUG_PRESETS);
  useEffect(() => {}, []);

  return (
    <Container>
      {data &
        data?.drugPresets.map((drugPreset) => (
          <GroupMedicament type="button" className="group"></GroupMedicament>
        ))}{" "}
      <Button className="add_button">Adicionar Linha</Button>
    </Container>
  );
};

export default ModalMedicamentGroup;
