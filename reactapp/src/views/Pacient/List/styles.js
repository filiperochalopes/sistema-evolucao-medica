import styled from "styled-components";

export default styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  margin-top: 2.625rem;
  margin-bottom: 2rem;
  flex: 1;
  align-self: stretch;

  .add_new_patient {
    max-width: 10.5rem;
  }

  .config {
    max-width: 8.75rem;
    align-self: flex-end;
  }

  .patients-container {
    margin-top: 2rem;
    flex: 0.5 1 0%;

    h2 {
      font-size: 1.5rem;
      margin-bottom: 2rem;
    }

    .patients {
      display: flex;
      flex-direction: column;
      row-gap: 0.5rem;
    }
  }
`;

export const PatientContent = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;

  button {
    height: 1.875rem;
  }

  .container_buttons {
    display: flex;
    column-gap: 0.625rem;
  }
`;
