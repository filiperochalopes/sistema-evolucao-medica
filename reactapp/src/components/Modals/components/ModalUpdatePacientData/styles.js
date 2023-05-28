import styled from "styled-components";

export default styled.form`
  padding: 1rem 0;
  display: flex;
  flex-direction: column;
  row-gap: 0.5rem;
  margin-top: 1.5rem;

  button {
    max-width: 14rem;
    align-self: flex-end;
    margin-top: 0.5rem;
  }

  .select_container {
    position: absolute;
    width: auto;
    width: calc(100% - 4rem);
  }
  .select_container_back {
    opacity: 0;
    user-select: none;
    pointer-events: none;
  }

  .row {
    display: flex;
    flex-wrap: wrap;
    column-gap: 0.5rem;
    row-gap: 0.5rem;

    .small {
      max-width: 11.125rem;
    }

    .larger {
      max-width: 20.125rem;
    }
    .normal {
      max-width: 14.5rem;
    }
  }
`;
