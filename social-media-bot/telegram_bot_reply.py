import requests
import time

BOT_TOKEN = "8010407290:AAHPnEWSBjoQCenXpUDjMCqwF5BaaoHPA9M"

def get_updates():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    return response.json()

def send_message(chat_id,message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=data)

print("Telegram Auto Reply Bot Started...")
last_update_id = None

while True:
    updates = get_updates()

    if "result" in updates:
        for update in updates["result"]:
            update_id = update["update_id"]

            if last_update_id is None or update_id > last_update_id:
                last_update_id = update_id

                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    user_text = update["message"].get("text", "").lower()

                    if user_text in ["hello", "hi", "hey" ]:
                        reply = "Hello! Welcome To Our Platform"

                    elif user_text == "price":
                        reply = "Please contact admin for pricing details."

                    else:
                        reply = "Thanks for your message 🙂 "

                    send_message(chat_id , reply)

    time.sleep(1) 

