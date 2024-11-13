import React, { useState } from "react";
import * as S from './BackgroundContainerStyles';
import MainContainer from "../main_container/MainContainer";
import InputAta from "../../../components/home/input_ata/InputAta";
import InputAudio from "../../../components/home/input_audio/InputAudio";
import ContainerTable from "../../table/ContainerTable";
import Button from "../../../components/home/button/Button";

const BackgroundContainer = () => {
    const [showTable, setShowTable] = useState(false);  

    const handleButtonClick = () => {
        setShowTable(true);  
    };

    return (
        <S.Background>
            <img src="../../src/assets/svg/logo.svg" alt="Logo" />
            {!showTable && (
                <MainContainer>
                    <InputAta />
                    <InputAudio />
                </MainContainer>
            )}

            {!showTable && (
                <Button onClick={handleButtonClick}>Exibir Tabela</Button>
            )}

            {showTable && <ContainerTable />}
        </S.Background>
    );
};

export default BackgroundContainer;
