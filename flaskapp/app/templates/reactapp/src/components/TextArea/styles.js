import styled from "styled-components";

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

  ::placeholder {
    color: ${({ theme }) => theme.colors.black};
  }
`;
