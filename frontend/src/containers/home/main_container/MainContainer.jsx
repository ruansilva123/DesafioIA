import React from "react";
import * as S from './MainContainerStyles'
import InputAta from "../../../components/home/input_ata/InputAta"; 
import InputAudio from "../../../components/home/input_audio/InputAudio";
import Button from "../../../components/home/button/Button";

const MainContainer = () =>{
    return(
        <S.LittleContainer>
            <img src= "../../src/assets/svg/logo.svg"/>
            <InputAta></InputAta>
            <InputAudio></InputAudio>
            <Button></Button>
        </S.LittleContainer>
    )
}

export default MainContainer