import styled from "styled-components";

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
    background: rgba(77, 76, 72, 0.8);
  }

  > div {
    z-index: 2;
    width: 100%;
    max-width: 37.5rem;
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
`;

export const Header = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  color: ${({ theme }) => theme.colors.white};
  align-items: center;
  margin-left: 2rem;
  justify-content: space-between;

  p {
    font-weight: 700;
    font-size: 1.25rem;
  }

  button {
    width: 2.5rem;
    height: 2.5rem;
    background-color: ${({ theme }) => theme.colors.red700};
    display: flex;
    align-items: center;
    justify-content: center;
  }
`;
