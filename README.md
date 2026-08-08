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
