import styled from "styled-components";

export default styled.div`
  margin: 2.625rem 0;
  width: 100%;
  display: flex;
  flex-direction: column;

  .row {
    display: flex;
    flex-wrap: wrap;
    column-gap: 0.5rem;
    row-gap: 0.5rem;

    .small {
      max-width: 11.125rem;
    }

    .larger {
      max-width: 22.71rem;
    }
    .normal {
      max-width: 14.5rem;
    }
  }
`;
