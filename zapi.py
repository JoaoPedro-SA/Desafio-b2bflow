from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from back import dados

app = Flask(__name__)

load_dotenv()

token = os.getenv("z_api_token")
instance = os.getenv("z_api_instance")

@app.route('/teste',methods=['GET'])
def teste():
    return jsonify({"message": "Hello, this is a test endpoint!"})

# https://api.z-api.io/instances/SUA_INSTANCIA/token/SEU_TOKEN/send-text
@app.route('/send-text', methods=['POST'])
def send_text():
     phone = dados['telefone']
     mensage = f"Ola {dados['nome']}, tudo bem com voce?"
     url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"
     payload = {
          "phone": phone,
          "message": mensage
     }
     headers = {
          "Content-Type": "application/json",
          "Client-Token": os.getenv("z_api_seguranca")
     }
     response = requests.post(url,json=payload,headers=headers)
     
     if response.status_code == 200:
          return jsonify(response.json()), 200
     else:
          return jsonify({"error": "Failed to send message", "details": response.text}), response.status_code
     
     
if __name__ == '__main__':
    app.run(debug=True)
