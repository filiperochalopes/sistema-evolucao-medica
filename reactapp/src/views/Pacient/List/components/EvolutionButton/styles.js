import styled from "styled-components";

export default styled.div`
  position: relative;
`;

export const PopUp = styled.div`
  width: 8rem;
  padding: 0.5rem;
  background: #fffae9;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  position: absolute;
  left: 0;
  font-size: 0.75rem;

  a {
    cursor: pointer;
    display: block;
    color: ${({ theme }) => theme.colors.black};
  }
`;
