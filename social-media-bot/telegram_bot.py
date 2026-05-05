import requests
BOT_TOKEN = "8010407290:AAHPnEWSBjoQCenXpUDjMCqwF5BaaoHPA9M"
CHAT_ID = "1524312789"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id" : CHAT_ID,
        "text" : message
    }

    response = requests.post(url, data=data)
    return response.json()

send_telegram_message("HELLO FROM SOCIAL MEDIA BOT 👍")