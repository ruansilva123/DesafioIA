import React, { useState } from "react";
import * as S from './InputAtaStyles';

const InputAta = ({ onFileChange }) => {  // Recebe a função de callback
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setSelectedFile(file);
            onFileChange(file);  // Passa o arquivo para o componente pai
        }
    };

    return (
        <S.ContainerInput>
            <S.FileInput 
                type="file"
                onChange={handleFileChange}
                id="file-upload"
            />
            <S.FileLabel htmlFor="file-upload">
                {selectedFile ? `Arquivo selecionado: ${selectedFile.name}` : 'Selecione o arquivo da ATA'}
            </S.FileLabel>
        </S.ContainerInput>
    );
};

export default InputAta;
