import styled from "styled-components";

export default styled.button`
  background-color: ${({ theme }) => theme.colors.blue};
  height: 2.5rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: ${({ theme }) => theme.colors.white};
`;
