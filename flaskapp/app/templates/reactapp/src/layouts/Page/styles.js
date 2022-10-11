import styled from "styled-components";

export default styled.div`
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
`;

export const Header = styled.header`
  background-color: ${({ theme }) => theme.colors.green};
  width: 100%;
  height: 5rem;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export const Main = styled.main`
  width: 100%;
  display: flex;
  flex: 1;
  justify-content: center;

  > div {
    width: 100%;
    max-width: 56.25rem;
    display: flex;
    align-items: baseline;
    justify-content: center;
  }
`;
