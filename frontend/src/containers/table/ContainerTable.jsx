import React from "react";
import * as S from './ContainerTableStyles'

const ContainerTable = ({ataFiles, audioFiles }) =>{
    return(
        <S.MainContainer>
            <S.TableContainer>
                <S.TableWrapper>
                    <S.StyledTable>
                        <thead>
                            <tr>
                                <S.TableHeader>Atendente</S.TableHeader>
                                <S.TableHeader>Forma de Pagamento</S.TableHeader>
                                <S.TableHeader>Compra Efetivada</S.TableHeader>
                                <S.TableHeader>ATA</S.TableHeader>
                                <S.TableHeader>Aúdio</S.TableHeader>
                            </tr>
                        </thead>
                        <tbody>
                                <S.TableRow>
                                    <S.TableCell>Claudio</S.TableCell>
                                    <S.TableCell>Ruan</S.TableCell>
                                    <S.TableCell>Sim</S.TableCell>
                                    <S.TableCell>Ata.pdf</S.TableCell>
                                    <S.TableCell>Audio1.mp3</S.TableCell>
                                </S.TableRow>
                        </tbody>
                    </S.StyledTable>
                </S.TableWrapper>
            </S.TableContainer>
        </S.MainContainer>
    )
}

export default ContainerTable