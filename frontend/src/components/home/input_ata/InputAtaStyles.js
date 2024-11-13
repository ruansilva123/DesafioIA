import styled from "styled-components";

export const ContainerInput = styled.div`
    width: 500px;
    height: 70px;
    background-color: #232625;
    outline: none;
    border: none;
    border-bottom: 2px solid rgba(255, 255, 255, 0.6);
    color: rgba(255, 255, 255, 0.6);
    background-image: url('../src/assets/svg/folder.svg');
    background-repeat: no-repeat;
    background-position: 430px;
    cursor: pointer;
    text-align: left;
    padding: 20px;
    margin-bottom: 25px;

    
    &:hover{
        border-bottom: 2px solid rgba(255, 255, 255, 0.8);
    }
    
`

export const FileInput = styled.input`
  display: none;
`;

export const FileLabel = styled.label`
  color: rgba(255, 255, 255, 0.6);
  cursor: pointer;
  display: flex;
  align-items: center;
  height: 100%;

  &:hover{
    color: rgba(255, 255, 255, 0.8);
  }

`;