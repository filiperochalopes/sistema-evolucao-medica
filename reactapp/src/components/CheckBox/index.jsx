import Container from "./styles";
import { AiOutlineCheck } from "react-icons/ai";

const CheckBox = ({ checked, ...rest }) => {
  return (
    <Container type="button" {...rest}>
      {checked && <AiOutlineCheck />}
    </Container>
  );
};

export default CheckBox;
