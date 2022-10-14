import styled, { css } from "styled-components";

export default styled.div`
  max-width: 100vw;
  max-height: 100vh;
  display: flex;
  flex-direction: column;
`;

export const Header = styled.header`
  background-color: ${({ theme }) => theme.colors.green};
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

  ${({ defaultHeight }) =>
    defaultHeight &&
    css`
      min-height: 5rem;

      img {
        height: 2.75rem;
      }
    `}
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
