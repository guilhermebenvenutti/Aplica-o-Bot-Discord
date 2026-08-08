import os
import requests

BASE = "https://discord.com/api/v10"


def _headers():
    return {
        "Authorization": f"Bot {os.environ['DISCORD_TOKEN']}",
        "Content-Type": "application/json",
    }


def testar_token() -> dict:
    """Teste A: confirma que o token é válido. Retorna o JSON do bot."""
    r = requests.get(f"{BASE}/users/@me", headers=_headers(), timeout=10)
    r.raise_for_status()
    return r.json()


def enviar_no_canal(canal_id: str, texto: str, componentes=None) -> str:
    """Teste B / uso real: envia mensagem a um canal e retorna o id_externo."""
    body = {"content": texto}
    if componentes:
        body["components"] = componentes

    r = requests.post(
        f"{BASE}/channels/{canal_id}/messages",
        headers=_headers(),
        json=body,
        timeout=10,
    )

    if r.status_code == 429:
        raise RuntimeError(f"rate limit: espere {r.json()['retry_after']}s")
    if not r.ok:
        raise RuntimeError(f"Discord {r.status_code}: {r.text}")

    return r.json()["id"]


def registrar_comando_barra(nome: str, descricao: str, opcoes: list | None = None) -> dict:
    """Parte D: registra (ou substitui) os slash commands do servidor de testes."""
    app_id = os.environ["DISCORD_APPLICATION_ID"]
    guild_id = os.environ["DISCORD_GUILD_ID"]

    comando = {"name": nome, "description": descricao}
    if opcoes:
        comando["options"] = opcoes

    r = requests.put(
        f"{BASE}/applications/{app_id}/guilds/{guild_id}/commands",
        headers=_headers(),
        json=[comando],  # PUT substitui a lista inteira de comandos do servidor
        timeout=10,
    )
    r.raise_for_status()
    return r.json()
