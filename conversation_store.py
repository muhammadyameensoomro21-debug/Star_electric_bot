from collections import defaultdict, deque

# Simple in-memory conversation context. It resets when the server restarts.
_history = defaultdict(lambda: deque(maxlen=12))

def get_history(user_id):
    return list(_history[user_id])

def add_exchange(user_id, user_text, bot_text):
    _history[user_id].append({"role": "user", "parts": [user_text]})
    _history[user_id].append({"role": "model", "parts": [bot_text]})
