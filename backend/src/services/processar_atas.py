from fastapi.exceptions import HTTPException
from fastapi import status
import pdfplumber
import os


def processar_atas(filename = None) -> str:
    
    try:
        router = os.path.abspath(f'files\\{filename}')

    except:
        raise HTTPException(
            detail = {'error' : f'O {filename} arquivo não foi encontrado!'},
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    pdf_content = ""

    with pdfplumber.open(router) as pdf:
        for page in pdf.pages:
            pdf_content += page.extract_text() + "\n"

    return pdf_content


# if __name__ == "__main__":
#     processar_atas("dia 1 - resumo.pdf")


# TESTE:

# pasta atual: PS C:\Users\ruanc\OneDrive\Documentos\GitHub\DesafioIA\backend>
# executar: python .\backend\src\services\attendants_names.py