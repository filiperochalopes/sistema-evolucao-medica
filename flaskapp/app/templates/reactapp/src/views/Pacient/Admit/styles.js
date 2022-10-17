import styled from "styled-components";

export default styled.form`
  margin: 2.625rem 0;
  width: 100%;
  display: flex;
  flex-direction: column;

  .add_pacient {
    max-width: 11.625rem;
  }

  .container_admit_data {
    margin: 3rem 0;
    display: flex;
    row-gap: 0.75rem;
    flex-direction: column;
  }

  .button_admit {
    max-width: 6.125rem;
    margin-top: 5.44rem;
    align-self: flex-end;
  }
`;

export const ContainerSearchInput = styled.div`
  display: flex;
  background-color: ${({ theme }) => theme.colors.gray};
  align-items: center;
  max-width: 28.5rem;
  padding-right: 0.5rem;
  margin: 1.5rem 0;
  input {
    padding-left: 1rem;
  }

  button {
    max-width: 6.875rem;
    height: 1.81rem;
  }
`;

const ContainerInputs = styled.div`
  padding: 1rem 0;
  display: flex;
  flex-direction: column;
  row-gap: 0.5rem;

  .row {
    display: flex;
    flex-wrap: wrap;
    column-gap: 0.5rem;

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

export const ContainerAddPacient = styled(ContainerInputs)`
  margin-top: 1.5rem;
  background-color: ${({ theme }) => theme.colors.grayLight};
`;
