from fastapi import status
from fastapi.exceptions import HTTPException
import google.generativeai as genai


genai.configure(api_key="")


def procurar_atendentes(text = None):

    if not text:
        raise HTTPException(
            detail = {'error' : 'Nenhum texto foi informado para extração de nomes!'},
            status_code = status.HTTP_400_BAD_REQUEST
        )

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content("diga olá?")
    print(response.text)