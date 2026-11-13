import os

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN", "")
    WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
    WHATSAPP_VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "change-this-token")
    GRAPH_API_VERSION = os.getenv("GRAPH_API_VERSION", "v22.0")
    OWNER_NAME = "Sadam Hussain"
    OWNER_PHONE = "03145810754"
    MAKER_NAME = "The Yameen's"
