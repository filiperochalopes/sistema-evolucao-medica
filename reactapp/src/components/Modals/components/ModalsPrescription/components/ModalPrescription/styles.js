import styled from "styled-components";

export default styled.form`
  flex: 1;
  padding: 2rem 0;
  display: flex;
  flex-direction: column;

  .medium_size {
    width: 13.5rem;
  }

  .container_medicaments {
    margin-top: 1.8rem;
    display: flex;
    flex-direction: column;
    row-gap: 0.5rem;

    .row {
      display: flex;
      flex-wrap: wrap;
      column-gap: 0.5rem;
    }

    .container_checkbox {
      display: flex;
      column-gap: 0.5rem;
      margin: 0.75rem 0;
    }
  }

  > button {
    align-self: flex-end;
    margin-top: 1rem;
  }
`;
