[README.md](https://github.com/user-attachments/files/30847262/README.md)
# Integração Discord — próximos passos

## 1. Instalar dependências
```
pip install -r requirements.txt
```

## 2. Configurar o .env
Copie `.env.example` para `.env` e preencha com os valores que você já tem
(token, public key, application id) mais o guild id e canal id (pegue com o
Modo Desenvolvedor ligado, botão direito > Copiar ID).

## 3. Teste A — o token funciona?
```
python scripts/testar_token.py
```
Espera-se `"bot": true` no JSON.

## 4. Teste B — primeira mensagem
```
python scripts/enviar_teste.py
```
Confira a mensagem aparecendo no canal.

## 5. Subir o servidor local
```
python -m app.main
```
Isso sobe o FastAPI na porta 3000 com o endpoint `/webhook/discord` pronto,
já validando a assinatura Ed25519.

## 6. Apontar o túnel
Como você já tem o cloudflared rodando, só confirme que ele está apontando
para `http://localhost:3000`.

## 7. Cadastrar a Interactions Endpoint URL no portal
No portal do Discord: **General Information → Interactions Endpoint URL** →
cole `https://SEU-TUNEL/webhook/discord` → Save Changes.
O Discord dispara um PING assinado na hora — se a resposta não for
`{"type": 1}`, ele recusa a URL. Com o servidor no ar, deve passar de primeira.

## 8. Registrar o slash command
```
python scripts/registrar_comando.py
```
Depois digite `/abrir` em algum canal do servidor de testes.

## 9. Se a internet cair (Plano B)
```
python scripts/gera_assinatura.py
```
Segue as instruções impressas — isso simula o PING do Discord localmente e
prova que a validação da assinatura funciona (aceita a válida, rejeita a
adulterada com 401). Print dos dois resultados = mesma nota que o Teste com
o portal real.

## O que falta fazer manualmente (não dá pra automatizar)
- Persistência real: trocar os `print()`/comentários `TODO` em `app/main.py`
  e `scripts/enviar_teste.py` pela gravação de fato na sua tabela `mensagens`
  (status: enfileirada → enviada/falha → respondida) e `canais_usuario`.
- Commit e tag:
  ```
  git switch -c feature/integracao-discord
  git add .
  git commit -m "feat: integracao com discord (envio + interactions)"
  git push -u origin feature/integracao-discord
  # depois do merge:
  git switch main && git pull
  git tag aula-05 && git push origin aula-05
  ```
