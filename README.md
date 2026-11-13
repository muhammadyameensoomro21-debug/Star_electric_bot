# STAR ELECTRIC WhatsApp AI Bot

A starter Flask webhook for Meta WhatsApp Cloud API + Google Gemini.

## Important
This project is **not connected to WhatsApp yet**. It becomes a real WhatsApp bot only after:
- A Meta developer app and WhatsApp Business Platform / Cloud API are configured.
- A public HTTPS webhook URL is deployed and subscribed to WhatsApp message events.
- Valid Meta access token, phone number ID, and verify token are configured.
- A Gemini API key is configured.

Use a WhatsApp Business number that the shop owner authorizes. Never share API keys publicly.

## Files
- `app.py`: Flask webhook routes
- `config.py`: settings and shop details
- `prompts.py`: Star Electric assistant instructions
- `conversation_store.py`: short in-memory conversation history
- `gemini_service.py`: Gemini response generation
- `whatsapp_service.py`: Meta webhook verification and message sending
- `requirements.txt`: Python dependencies
- `.env.example`: environment-variable template

## Run locally
1. Install Python 3.10+.
2. Create a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in credentials.
5. Run: `python app.py`

For production, deploy with a public HTTPS URL and run:
`gunicorn app:app`

Set the Meta webhook callback URL to `https://YOUR-DOMAIN/webhook`, use the same verify token as `WHATSAPP_VERIFY_TOKEN`, and subscribe to the `messages` webhook field.

## Safety and pricing
The assistant gives approximate product guidance only. Add a verified shop price list before relying on exact prices. It refuses dangerous DIY instructions for mains electrical repairs and directs customers to a qualified electrician.
