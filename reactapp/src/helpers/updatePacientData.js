import ModalUpdatePacientData from "components/Modals/components/ModalUpdatePacientData";

const updatePacientData = (id) => ({
  confirmButtonAction: () => {},
  content: <ModalUpdatePacientData id={id} />,
  returnButtonAction: () => {},
  title: "Atualizar Dados do Paciente",
});

export default updatePacientData;
