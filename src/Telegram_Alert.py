import requests
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

load_dotenv()
token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("CHAT_ID")

def Telegram_Alert(message):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = { 'chat_id': chat_id, 'text': message}

        response = requests.post(url, data)
        response.raise_for_status() # Raises error.
        logging.info("Message sent successfully.")

    except Exception as e:
        logging.error(f"Message failed: {e}")
