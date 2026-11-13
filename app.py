import os
from flask import Flask, request
from dotenv import load_dotenv
from config import Config
from whatsapp_service import verify_webhook, send_whatsapp_message
from gemini_service import get_bot_reply

load_dotenv()
app = Flask(__name__)

@app.get("/")
def home():
    return "STAR ELECTRIC WhatsApp bot server is running."

@app.get("/webhook")
def webhook_verify():
    ok, response = verify_webhook(request.args)
    return (response, 200) if ok else (response, 403)

@app.post("/webhook")
def webhook_receive():
    data = request.get_json(silent=True) or {}
    # Acknowledge Meta quickly; process text messages in this request.
    try:
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                for message in value.get("messages", []):
                    sender = message.get("from")
                    text = message.get("text", {}).get("body", "")
                    if sender and text:
                        reply = get_bot_reply(sender, text)
                        send_whatsapp_message(sender, reply)
    except Exception as exc:
        app.logger.exception("Webhook processing failed: %s", exc)
    return "EVENT_RECEIVED", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
