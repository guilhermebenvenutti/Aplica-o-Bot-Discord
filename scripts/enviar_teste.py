"""Teste B — roda: python scripts/enviar_teste.py
Envia uma mensagem de teste ao canal configurado no .env."""
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

from app.services.discord import enviar_no_canal

if __name__ == "__main__":
    canal_id = os.environ["DISCORD_CANAL_ID"]
    id_externo = enviar_no_canal(canal_id, "Primeira mensagem do bot!")
    print(f"Mensagem enviada. id_externo = {id_externo}")
    # Aqui é onde, no projeto real, você atualizaria o registro no banco:
    # status = "enviada", id_externo = id_externo
