import React from "react";
import * as S from './MainContainerStyles'
import InputAta from "../../../components/home/input_ata/InputAta"; 
import InputAudio from "../../../components/home/input_audio/InputAudio";

const MainContainer = ({children}) =>{
    return(
        <S.LittleContainer>
            {children}
        </S.LittleContainer>
    )
}

export default MainContainer