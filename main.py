import os
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def home():
    return "Bot Receiver Active!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def receive_update():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    message = data["message"]["text"]

    reply = f"Sweeti bol rahi hai: Tumne kaha - {message}"
    
    requests.post(API_URL, json={
        "chat_id": chat_id,
        "text": reply
    })

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)