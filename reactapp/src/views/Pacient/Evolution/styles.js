import styled from "styled-components";

export default styled.div`
  margin: 2.625rem 0;
  width: 100%;

  h2 {
    font-size: 1.5rem;
    font-weight: 400;
  }

  .legend {
    color: ${({ theme }) => theme.colors.gray};
  }

  .button_normal {
    max-width: 11.75rem;
  }

  .evolution {
    &_pacient {
      display: flex;
      flex-direction: column;
      row-gap: 1rem;

      .header {
        display: flex;
        justify-content: space-between;

        button {
          max-width: 13.8rem;
          height: 1.875rem;
        }
      }

      .row {
        display: flex;
        column-gap: 0.75rem;

        .normal {
          max-width: 15.5rem;
        }

        .larger {
          max-width: 27.5rem;
        }

        .small {
          max-width: 12rem;
        }
      }

      .legend {
        margin-top: 0.25rem;
      }
    }

    &_button {
      max-width: 6.125rem;
      margin-top: -0.5rem;
      align-self: flex-end;
    }
  }

  .prescriptions_pacient {
    display: flex;
    flex-direction: column;
    margin-top: 1rem;

    h2 {
      margin-bottom: 1rem;
    }

    ol {
      display: flex;
      flex-direction: column;
      row-gap: 0.5rem;
      margin-left: 2rem;

      .error {
        margin-top: 0.25rem;
        font-size: 0.625rem;
        color: ${({ theme }) => theme.colors.red};
      }
    }

    .legend {
      margin-top: 0.5rem;
    }

    .buttons {
      display: flex;
      justify-content: flex-end;
      column-gap: 0.5rem;
      margin-top: 0.75rem;
      margin-bottom: 0.5rem;

      .button_add_prescription {
        width: 18.25rem;
      }
    }
    .button-update_prescription {
      align-self: flex-end;
    }
  }

  .pendencies_pacient {
    display: flex;
    flex-direction: column;
    margin-top: 1rem;

    h2 {
      margin-bottom: 1rem;
    }

    .legend {
      margin-top: 0.75rem;
    }

    .button-update_pendencies {
      align-self: flex-end;
      margin-top: 1.5rem;
    }
  }
`;

export const ContainerListOption = styled.div`
  width: 100%;
  justify-content: space-between;
  display: flex;

  .column {
    flex-direction: column;
    row-gap: 0.5rem;
  }

  button {
    background: none;
    border: none;
    cursor: pointer;
  }

  > div {
    display: flex;
    column-gap: 0.5rem;
  }
`;
