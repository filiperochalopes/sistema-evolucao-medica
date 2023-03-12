import styled, { css } from "styled-components";

export default styled.button`
  height: 2.5rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  padding: 0 0.5rem;
  cursor: pointer;

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
