import styled from "styled-components";

export default styled.li`
  width: 100%;
  margin: 0 2rem;
  height: 9.3rem;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  row-gap: 0.5rem;
  background-color: #d9d9d9;
  list-style: none;

  input[type="radio"]:checked + label {
    border: 2px solid ${({ theme }) => theme.colors.green};
  }
`;
