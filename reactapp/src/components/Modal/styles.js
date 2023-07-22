import styled, { css } from "styled-components";

export default styled.div`
  width: 100vw;
  height: 100vh;
  z-index: 5;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;

  .button-modal {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(5px);
  }

  > div {
    z-index: 2;
    width: 100%;
    max-width: 37.5rem;
    border: 1px solid #d9d9d9;
    box-shadow: 0px 4px 35px 10px rgba(0, 0, 0, 0.1);
  }

  .content,
  .content-main {
    background-color: #fff;
  }
`;

export const ContainerContentModal = styled.div`
  display: flex;
  background: #fff;
  flex-direction: column;
  border-radius: 5px;

  main {
    overflow: auto;
  }
`;

export const Header = styled.div`
  background-color: ${({ theme }) => theme.colors.green};
  width: 100%;
  justify-content: space-between;
  line-height: 2.5rem;
  display: flex;
  color: #fff;

  p {
    font-weight: 700;
    font-size: 1.25rem;
    width: 100%;
    padding-left: 2rem;
  }

  button {
    width: 2.5rem;
    height: 2.5rem;
    background-color: ${({ theme }) => theme.colors.red700};
    display: flex;
    align-items: center;
    cursor: pointer;
    justify-content: center;
  }

  ${({ headerStyle, theme }) => {
    switch (headerStyle) {
      case "red":
        return css`
          background-color: ${theme.colors.red700};
        `;
      default:
        return css`
          background-color: ${theme.colors.green};
        `;
    }
  }}
`;

export const Main = styled.main`
  width: 100%;
  display: flex;
  flex: 1;
  justify-content: center;
  padding: 0 2rem;
  max-height: 500px;
  overflow-y: auto;

  > div {
    width: 100%;
    max-width: 56.25rem;
    display: flex;
    align-items: baseline;
    justify-content: center;
  }
`;
