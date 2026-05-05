import requests
import os
from dotenv import load_dotenv

# .env load karo
load_dotenv()

# env se values lo
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)
    return response.json()

send_telegram_message("HELLO FROM SOCIAL MEDIA BOT 👍")