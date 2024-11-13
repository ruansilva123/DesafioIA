import React from "react";
import * as S from './ButtonStyles'

const Button = ({onClick, children}) =>{
    return(
        <S.ButtonContainer onClick={onClick}>
            {children} 
        </S.ButtonContainer>
    )
}

export default Button