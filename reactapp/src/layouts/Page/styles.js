import styled, { css } from "styled-components";

export default styled.div`
  max-width: 100vw;
  max-height: 100vh;
  display: flex;
  height: 100%;
  flex-direction: column;
`;

export const Header = styled.header`
  background-color: ${({ theme }) => theme.colors.green};
  width: 100%;
  justify-content: center;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 2rem;
  min-height: 5rem;

  ul {
    position: absolute;
    right: 2rem;
    top: 2rem;
    list-style: none;

    ul {
      position: absolute;
      top: 1em;
      width: 150px;

      li {
        width: 100%;
        padding: 1rem;
        background-color: ${({ theme }) => theme.colors.gray};
      }
    }
  }
`;

export const Main = styled.main`
  width: 100%;
  display: flex;
  flex: 1;
  justify-content: center;
  padding: 0 2rem;

  > div {
    width: 100%;
    max-width: 56.25rem;
    display: flex;
    align-items: baseline;
    justify-content: center;
  }
`;
