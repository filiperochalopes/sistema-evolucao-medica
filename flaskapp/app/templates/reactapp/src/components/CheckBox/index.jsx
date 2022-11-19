import Container from "./styles";
import { AiOutlineCheck } from "react-icons/ai";

const CheckBox = ({ checked }) => {
  return <Container type="button">{checked && <AiOutlineCheck />}</Container>;
};

export default CheckBox;
