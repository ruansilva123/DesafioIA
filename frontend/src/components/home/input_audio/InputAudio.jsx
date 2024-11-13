import React, { useState } from "react";
import * as S from './InputAudioStyles';

const InputAudio = ({ onFileChange }) => {
    const [selectedAudio, setSelectedAudio] = useState([]); // Inicializa como array vazio

    const handleFileChange = (e) => {
        const files = e.target.files;
        if (files) {
            const fileArray = Array.from(files);  // Converte FileList para array
            setSelectedAudio(fileArray);
            onFileChange(fileArray);  // Passa os arquivos para o componente pai
        }
    };

    return (
        <S.ContainerInputAudio>
            <S.FileInputAudio
                type="file"
                multiple
                onChange={handleFileChange}
                id="file-audio"
            />
            <S.FileLabel htmlFor="file-audio">
                {selectedAudio.length > 0 ? (
                    <S.FileNames>
                        Áudios selecionados: 
                        {selectedAudio.map((file, index) => (
                            <S.FileName key={index}>{file.name}</S.FileName>
                        ))}
                    </S.FileNames>
                ) : (
                    'Selecione os arquivos de áudio'
                )}
            </S.FileLabel>
        </S.ContainerInputAudio>
    );
};

export default InputAudio;
