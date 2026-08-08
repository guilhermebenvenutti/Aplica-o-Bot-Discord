"""Parte D — roda: python scripts/registrar_comando.py
Registra o slash command /abrir no servidor de testes.
Comandos de servidor (guild) aparecem na hora; comandos globais podem levar até 1h."""
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

from app.services.discord import registrar_comando_barra

if __name__ == "__main__":
    opcoes = [{
        "type": 3,  # STRING
        "name": "assunto",
        "description": "Descreva o problema",
        "required": True,
    }]
    resultado = registrar_comando_barra("abrir", "Abre um chamado de suporte", opcoes)
    print(resultado)
    print("\nOK — vá no Discord e digite /abrir no canal do servidor do grupo.")
