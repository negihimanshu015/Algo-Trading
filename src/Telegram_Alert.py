import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("CHAT_ID")

def Telegram_Alert(message):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = { 'chat_id': chat_id, 'text': message}

        response = requests.post(url, data)
        response.raise_for_status()
    except Exception as e:
        print(f"Error Occured: {e}")