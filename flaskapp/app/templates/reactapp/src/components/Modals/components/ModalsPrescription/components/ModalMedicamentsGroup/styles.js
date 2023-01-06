import styled, { css } from "styled-components";

export default styled.div`
  padding: 2rem 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;

  .add_button {
    margin-top: 1rem;
    max-width: 13.1rem;
  }
`;

export const GroupMedicament = styled.button`
  width: 100%;
  margin: 0 2rem;
  height: 9.3rem;

  background-color: #d9d9d9;

  ${({ selected }) =>
    selected &&
    css`
      border: 4px solid #325aa4;
    `}
`;
