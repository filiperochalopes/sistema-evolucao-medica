import styled from "styled-components";

export default styled.div`
  width: 100%;
  margin: 2.75rem 0;

  h2 {
    font-size: 1.5rem;
    font-weight: 400;
    margin-bottom: 1.5rem;

    &.secondary {
      color: ${({ theme }) => theme.colors.gray400};
    }
  }

  p {
    color: ${({ theme }) => theme.colors.gray400};
    font-size: 1.25rem;
    margin-bottom: 1rem;
  }

  .header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.875rem;

    button {
      max-width: 13.8rem;
      height: 1.875rem;
    }
  }

  ol,
  ul {
    margin-left: 2rem;
    margin-bottom: 2rem;

    li {
      font-size: 1.25rem;
      color: ${({ theme }) => theme.colors.gray400};
    }
  }

  ul {
    list-style: none;
    margin-left: 0;
  }
`;
