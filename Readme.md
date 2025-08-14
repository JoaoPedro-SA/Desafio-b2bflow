# Desafio_b2bflow

## Tabela Supabase

| id  | nome              | telefone         |
| --- | ----------------- | ---------------- |
| 1   | João Pedro        | 5511986293358    |
| 2   | Marcelo B\*\*\*\* | 55**\*\*\***4809 |

## Variáveis de ambiente

### Z-API

- z_api_token="SUA_CHAVE_Z_API"
- z_api_instance="SUA_INSTANCIA_Z_API"
- z_api_seguranca="SUA_CHAVE_DE_SEGURANCA"

### Supabase

- SUPABASE_URL=https://seu-projeto.supabase.co
- SUPABASE_KEY=SUA_CHAVE_SUPABASE

## Como rodar

1- faça um git clone: https://github.com/JoaoPedro-SA/Desafio-b2bflow.git

2- faça o pip install do requeriments.txt

3- execultar o servidor do arquivo zapi.py

4- execultar esse endpoint no Postman: POST => http://127.0.0.1:5000/send-text

O codigo já esta configurado para enviar a msg para o recrutador.
