import os
from dotenv import load_dotenv
from supabase import create_client, Client
import time


load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Variáveis SUPABASE_URL e SUPABASE_KEY não definidas.")

supabase: Client = create_client(url, key)


# Testando
data = supabase.table("contacts").select("*").execute()
print("Full response:", data)
print("Data:", data.data)


# while True:
#      response = supabase.table("contacts").select("*").execute()
#      print("Dados atuais:", response.data)
#      time.sleep(5)


response = (
    supabase.table("contacts")
    .select("*")
    .execute()
    
)

print(response.data)
print(response.count)

