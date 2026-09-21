import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise SystemExit("GEMINI_API_KEY nao encontrada. Copie o .env.example para .env e preencha a chave.")


def testAPI(pergunta: str | None = None):
    client = genai.Client(api_key=API_KEY)

    if pergunta is None:
        pergunta = input("Digite sua pergunta: ")

    try:
        resposta = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=pergunta,
        )
    except errors.ServerError:
        print("Servidor sobrecarregado. Tentando mais uma vez em 2 segundos...")
        time.sleep(2)
        resposta = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=pergunta,
        )

    print(resposta.text)

    uso = resposta.usage_metadata
    print()
    print("--- tokens usados ---")
    print(f"pergunta   : {uso.prompt_token_count}")
    print(f"raciocinio : {uso.thoughts_token_count}")
    print(f"resposta   : {uso.candidates_token_count}")
    print(f"total      : {uso.total_token_count}")


testAPI()
