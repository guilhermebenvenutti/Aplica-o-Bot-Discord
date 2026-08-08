"""Teste A — roda: python scripts/testar_token.py
Confirma que o token funciona antes de tentar qualquer outra coisa."""
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

from app.services.discord import testar_token

if __name__ == "__main__":
    dados = testar_token()
    print(dados)
    assert dados.get("bot") is True, "resposta não tem bot: true — confira o token"
    print("\nOK — token válido.")
