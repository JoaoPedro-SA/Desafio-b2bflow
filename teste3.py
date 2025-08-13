from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

token = os.getenv("z_api_token")
instance = os.getenv("z_api_instance")


@app.route('/teste',methods=['Get'])
def teste():
    return jsonify({"message": "Hello, this is a test endpoint!"})

# https://api.z-api.io/instances/SUA_INSTANCIA/token/SEU_TOKEN/send-text
# http://127.0.0.1:5000/instances/3E59DCD57962C0FE157FDE1025393F89/token/334D817480720ADF672284AB/send-text
@app.route(f'/send-text', methods=['Get'])
def teste2():
     return jsonify({
          "instance": instance,
          "token": token,
     })

@app.route('/sendText2', methods=['POST'])
def send_text2():
     dados = request.get_json()
     phone = dados.get('phone')
     message = dados.get('message')
     return jsonify({
          "phone": phone,
          "message": message,
     })

@app.route('/send-text', methods=['POST'])
def send_text():
     dados = request.get_json()
     phone = dados.get('phone')
     message = dados.get('message')
     url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"
     payload = {
          "phone": phone,
          "message": message
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
    print("Server is running...") 