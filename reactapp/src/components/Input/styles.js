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
  position: relative;
`;

export const Label = styled.label`
  width: calc(100% - 8px);
  background: ${({ theme }) => theme.colors.gray};
  color: ${({ theme }) => theme.colors.black};
  position: absolute;
  transition: top 0.2s linear, left 0.2s linear, font-size 0.2s linear;
  font-size: 1rem;
  top: 10px;
  left: 8px;
  pointer-events: none;
  user-select: none;
  ${({ select }) =>
    select &&
    css`
      top: 4px;
      font-size: 0.5rem;
    `}
  ${({ disabled }) =>
    disabled &&
    css`
      background: #ececec;
    `}
`;
