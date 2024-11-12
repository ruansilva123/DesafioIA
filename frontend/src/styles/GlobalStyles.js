import { createGlobalStyle } from 'styled-components';

export const GlobalStyles = createGlobalStyle`
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-size: 18px;
    }
    
    body {
        font-family: 'Tahoma', 'Arial', 'Sans-serif';
        
    }
    a {
        text-decoration: none;
        color: inherit;
    }
    ul {
        list-style: none;
    }
 
`;