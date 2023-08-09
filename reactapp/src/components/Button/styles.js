import styled, { css, keyframes } from "styled-components";

const spin = keyframes`
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
`;

export const ContainerLoading = styled.div`
  ${({ loading }) =>
    loading &&
    css`
      svg {
        animation: ${spin} 0.8s infinite linear;
      }
    `}
`;

export default styled.button`
  height: 2.5rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  padding: 0 0.5rem;
  cursor: pointer;

  &.small {
    max-width: 6.125rem;
    margin-top: 5.44rem;
    align-self: flex-end;
  }

  ${({ customType }) => {
    switch (customType) {
      case "gray":
        return css`
          background-color: ${({ theme }) => theme.colors.grayMedium};
          color: ${({ theme }) => theme.colors.black};
        `;
      case "gray-300":
        return css`
          background-color: ${({ theme }) => theme.colors.gray};
          color: ${({ theme }) => theme.colors.black};

          :hover {
            background-color: #e9e9e9;
          }
        `;
      case "red":
        return css`
          background-color: ${({ theme }) => theme.colors.red700};
          color: ${({ theme }) => theme.colors.white};
        `;
      default:
        return css`
          background-color: ${({ theme }) => theme.colors.blue};
          color: ${({ theme }) => theme.colors.white};
        `;
    }
  }}
`;
