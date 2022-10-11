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
