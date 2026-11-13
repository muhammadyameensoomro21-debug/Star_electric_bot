from google import genai
from config import Config
from prompts import SYSTEM_PROMPT
from conversation_store import get_history, add_exchange

def get_bot_reply(user_id, user_text):
    if not Config.GEMINI_API_KEY:
        return "Maazrat, Star Electric assistant abhi configure nahi hua. Barah-e-karam shop se rabta karein: 03145810754"
    try:
        client = genai.Client(api_key=Config.GEMINI_API_KEY)
        history = get_history(user_id)
        contents = []
        for item in history:
            contents.append({"role": item["role"], "parts": item["parts"]})
        contents.append({"role": "user", "parts": [user_text]})
        response = client.models.generate_content(
            model=Config.GEMINI_MODEL,
            contents=contents,
            config={"system_instruction": SYSTEM_PROMPT, "temperature": 0.4}
        )
        answer = (response.text or "").strip()
        if not answer:
            answer = "Maazrat, main abhi jawab tayyar nahi kar saka. Aap 03145810754 par shop se rabta kar sakte hain."
        add_exchange(user_id, user_text, answer)
        return answer[:4000]
    except Exception:
        return "Maazrat, filhal technical masla aa raha hai. Barah-e-karam kuch dair baad koshish karein ya 03145810754 par rabta karein."
