python
import asyncio
import schedule
from pyrogram import Client
import time
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = "my_account"

groups = os.getenv("GROUPS").split(",")
message_text = os.getenv("MESSAGE_TEXT", "Привіт! Це тестове повідомлення.")

async def send_messages():
    async with Client(session_name, api_id, api_hash) as app:
        for group in groups:
            try:
                await app.send_message(group, message_text)
                print(f"✅ Повідомлення відправлено в {group}")
            except Exception as e:
                print(f"❌ Помилка в {group}: {e}")

def job():
    asyncio.run(send_messages())

schedule.every(1).hours.do(job)

print("📢 Бот запущено на Railway!")
while True:
    schedule.run_pending()
    time.sleep(60)
