import styled from "styled-components";

export default styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  margin-top: 2.625rem;
  margin-bottom: 2rem;
  flex: 1;
  align-self: stretch;

  .add_new_pacient {
    max-width: 10.5rem;
  }

  .config {
    max-width: 8.75rem;
    align-self: flex-end;
  }

  .pacients-container {
    margin-top: 2rem;
    flex: 1;

    h2 {
      font-size: 1.5rem;
      margin-bottom: 2rem;
    }

    .pacients {
      display: flex;
      flex-direction: column;
      row-gap: 0.5rem;
    }
  }
`;

export const PacientContent = styled.div`
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

    .container_button_relative {
      position: relative;
    }
  }
`;
