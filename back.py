import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Variáveis SUPABASE_URL e SUPABASE_KEY não definidas.")

supabase: Client = create_client(url, key)

response = (
    supabase.table("contacts")
    .select("*")
    .execute()
    
)

usuarios = []
for contato in response.data:
    usuarios.append({
        "nome": contato["nome"],
        "telefone": contato["telefone"]
    })

# João - Candidato
#dados = usuarios[0]
# Marcelo - Recrutador
dados = usuarios[1]

# print(dados)
