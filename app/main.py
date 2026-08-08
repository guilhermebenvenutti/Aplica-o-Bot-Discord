import os
import json

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request, Response
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

app = FastAPI()

verify_key = VerifyKey(bytes.fromhex(os.environ["DISCORD_PUBLIC_KEY"]))


@app.post("/webhook/discord")
async def discord_webhook(req: Request):
    sig = req.headers.get("X-Signature-Ed25519", "")
    ts = req.headers.get("X-Signature-Timestamp", "")
    body = await req.body()  # corpo CRU, em bytes — não use req.json() aqui

    try:
        verify_key.verify(ts.encode() + body, bytes.fromhex(sig))
    except (BadSignatureError, ValueError):
        return Response(status_code=401)

    interaction = json.loads(body)
    tipo = interaction["type"]

    if tipo == 1:
        # PING que o Discord manda ao validar/registrar a URL
        return {"type": 1}

    if tipo == 2:
        # slash command (ex.: /abrir assunto:"impressora")
        assunto = interaction["data"]["options"][0]["value"]
        usuario_id = interaction["member"]["user"]["id"]
        # TODO: gravar no banco (status = "enfileirada" -> processar sem await
        # se demorar, para não estourar os 3 segundos de prazo)
        print(f"/abrir chamado por {usuario_id}: {assunto}")
        return {"type": 4, "data": {"content": f"Recebido: {assunto}"}}

    if tipo == 3:
        # clique em botão/componente
        custom_id = interaction["data"]["custom_id"]
        # TODO: gravar a confirmação no banco (status = "respondida")
        print(f"Componente clicado: {custom_id}")
        return {"type": 7, "data": {"content": "Confirmado!", "components": []}}

    return Response(status_code=400)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=3000, reload=True)
