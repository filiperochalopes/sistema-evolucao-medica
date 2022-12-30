import styled from "styled-components";

export default styled.form`
  width: 100%;
  display: flex;
  flex-direction: column;
  margin: 2.5rem 0;

  h2 {
    font-weight: 400;
    font-size: 1.5rem;
    margin-bottom: 3.75rem;
  }

  .input {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    flex-wrap: wrap;

    > p {
      width: 100%;
      max-width: 15.25rem;
    }
  }

  button {
    align-self: flex-end;
    max-width: 13rem;
    margin-top: 5rem;
  }
`;

export const Inputs = styled.div`
  display: flex;
  column-gap: 0.5rem;
  flex: 1;

  input {
    max-width: 15.25rem;
  }
  .small {
    max-width: 3.75rem;
    min-width: 3.75rem;
  }
  > div {
    display: flex;
    align-items: center;
    column-gap: 0.5rem;
  }
`;
