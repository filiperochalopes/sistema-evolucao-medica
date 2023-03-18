import styled, { css } from "styled-components";

export default styled.input`
  height: 2.5rem;
  display: flex;
  align-items: center;
  padding-left: 0.5rem;
  border: none;
  width: 100%;
  outline: none;
  font-size: 1rem;
  background: ${({ theme }) => theme.colors.gray};

  ::placeholder {
    color: ${({ theme }) => theme.colors.black};
  }
  :disabled {
    background: #ececec;
  }
`;

export const ContainerInput = styled.div`
  flex: 1;
`;
