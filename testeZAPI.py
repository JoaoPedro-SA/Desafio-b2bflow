from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

token = os.getenv("Z_API_TOKEN")
instance = os.getenv("Z_API_INSTANCE")

@app.route('/send-text', methods=['POST'])
def send_text():
    data = request.json
    phone = data.get('5511986293358')
    message = data.get('Ola aqui e o Robozito.')
    
    if not phone or not message:
        return jsonify({"error": "Phone and message are required"}), 400
    
    zapi_url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"
    payload = {
        "phone": phone,
        "message": message
    }
    headers = {
        "Content-Type": "application/json",
        "Client-Token": os.getenv("Z_API_CLIENT_TOKEN")
    }
    
    response = requests.post(zapi_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to send message", "details": response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
