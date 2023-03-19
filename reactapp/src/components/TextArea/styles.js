import styled, { css } from "styled-components";

export default styled.textarea`
  background: ${({ theme }) => theme.colors.gray};
  width: 100%;
  height: 11rem;
  display: flex;
  align-items: center;
  padding: 0.5rem 0.5rem;
  border: none;
  outline: none;
  font-size: 1rem;
  resize: none;
  padding-top: 1rem;

  ::placeholder {
    color: ${({ theme }) => theme.colors.black};
  }
`;

export const ContainerTextArea = styled.div`
  position: relative;
`;

export const Label = styled.label`
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
