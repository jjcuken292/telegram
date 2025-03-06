from telethon import TelegramClient
import asyncio

api_id = '20139205'
api_hash = 'fab8db9897ed148dbb4da62e77621ff4'
phone_number = '+380634398931'
groups = ['@Crypto_Affiliate_eng', '@fortraffic']
message = """🎯  PREMIUM LIVE LEADS ..."""  # Твій текст повідомлення

async def send_messages():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone=phone_number)
    for group in groups:
        try:
            await client.send_message(group, message)
            print(f"Повідомлення відправлено у групу: {group}")
        except Exception as e:
            print(f"Помилка: {e}")
    await client.disconnect()

async def main():
    while True:
        await send_messages()
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())