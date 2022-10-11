import styled from "styled-components";

export default styled.input`
  background: ${({ theme }) => theme.colors.gray};
  width: 100%;
  height: 2.5rem;
  display: flex;
  align-items: center;
  padding-left: 0.5rem;
  border: none;
  outline: none;
  font-size: 1rem;

  ::placeholder {
    color: ${({ theme }) => theme.colors.black};
  }
`;
