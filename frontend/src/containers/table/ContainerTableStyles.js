import styled from "styled-components";

export const MainContainer = styled.div`
    width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`

export const TableContainer = styled.div`
    width: 80%;
    margin: 20px auto;
    background-color: #232625;
    box-shadow: 0 2px 10px ;
    border-radius: 8px;
    overflow: hidden;
`;

export const TableWrapper = styled.div`
    max-height: 500px; 
    overflow-y: auto; 
`;

export const StyledTable = styled.table`
    width: 100%;
    border-collapse: collapse;

    th, td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid;
    }

    th {
        background-color: #6DA021;
        color: #232625;
        font-weight: bold;
    }

    tr:hover {
        background-color: #181A19;
    }

    td {
        color: rgba(255, 255, 255, 0.6);
        border-bottom: none;
    }

`;

export const TableHeader = styled.th`
    color: white;
    padding: 10px;
`;

export const TableRow = styled.tr`
    &:hover {
        background-color: black;
    }
`;

export const TableCell = styled.td`
    padding: 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.6);
`;