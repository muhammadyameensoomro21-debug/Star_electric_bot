import requests
from config import Config

def verify_webhook(args):
    mode = args.get("hub.mode")
    token = args.get("hub.verify_token")
    challenge = args.get("hub.challenge")
    if mode == "subscribe" and token == Config.WHATSAPP_VERIFY_TOKEN and challenge:
        return True, challenge
    return False, "Verification failed"

def send_whatsapp_message(to, body):
    if not Config.WHATSAPP_TOKEN or not Config.WHATSAPP_PHONE_NUMBER_ID:
        raise RuntimeError("WhatsApp Cloud API credentials are missing.")
    url = (
        f"https://graph.facebook.com/{Config.GRAPH_API_VERSION}/"
        f"{Config.WHATSAPP_PHONE_NUMBER_ID}/messages"
    )
    headers = {
        "Authorization": f"Bearer {Config.WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": body},
    }
    response = requests.post(url, headers=headers, json=payload, timeout=20)
    response.raise_for_status()
    return response.json()
