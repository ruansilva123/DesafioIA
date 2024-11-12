from fastapi.exceptions import HTTPException
from fastapi import status
import pdfplumber
import os


def processar_atas(routers = []):
    
    if not routers:
        raise HTTPException(
            detail = {'error' : 'Nenhuma ATA foi encontrada!'},
            status_code = status.HTTP_400_BAD_REQUEST
        )

    pdfs_content = ""

    for router in routers: 

        with pdfplumber.open(router) as pdf:
            for page in pdf.pages:
                pdfs_content += page.extract_text() + "\n"

    return pdfs_content


# if __name__ == "__main__":
#     teste = os.path.abspath("docs\\dia 1 - resumo.pdf")
#     processar_atas([teste])


"""
TESTE:

pasta atual: PS C:\Users\ruanc\OneDrive\Documentos\GitHub\DesafioIA\backend>
executar: python .\backend\src\services\attendants_names.py
"""