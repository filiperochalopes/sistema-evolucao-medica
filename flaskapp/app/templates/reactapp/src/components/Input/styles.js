import styled from "styled-components";

export default styled.input`
  height: 2.5rem;
  display: flex;
  align-items: center;
  padding-left: 0.5rem;
  border: none;
  outline: none;
  font-size: 1rem;
  background: ${({ theme }) => theme.colors.gray};

  ::placeholder {
    color: ${({ theme }) => theme.colors.black};
  }
`;

export const ContainerInput = styled.div`
  flex: 1;
  background: ${({ theme }) => theme.colors.gray};
`;
