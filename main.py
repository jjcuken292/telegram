from telethon import TelegramClient, errors
import asyncio
import os
from dotenv import load_dotenv

# Завантаження змінних середовища
load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

# Список груп
GROUPS = [
    '@Crypto_Affiliate_eng', '@fortraffic', '@LeadsAreUs', '@affmktcity',
    '@affiliate_marketing_hub', '@blackhat_forever', '@wiseaffiliate',
    '@delta_fx_crypto_board', '@trafficforyou', '@enalltrafficgroupchat',
    '@looking_for_offers', '@dark_side_affiliate_offers', '@affhub_collab',
    '@affcommunity', '@forex_and_crypto_leads_board', '@AffiliateChat',
    '@thegodsforexcrypto', '@affiliatecryptoconference', '@affiliatebro',
    '@trafficforeveryone', '@TrafficPlaceMarket', '@GodsOfFx',
]

# Текст повідомлення
MESSAGE = """🎯 PREMIUM LIVE LEADS
🚀 Get high-quality, real-time leads that bring results!

I work with a wide range of geos and offer flexible deals to fit your needs. Whether you want high-intent traffic or exclusive leads, I can help you scale!

🌍 Top geos available:

🇩🇪 Germany | 🇫🇷 France | 🇮🇹 Italy | 🇪🇸 Spain | 🇳🇱 Netherlands
🇸🇪 Sweden | 🇳🇴 Norway | 🇩🇰 Denmark | 🇨🇭 Switzerland | 🇬🇧 United Kingdom
🇧🇪 Belgium | 🇦🇹 Austria | 🇫🇮 Finland | 🇵🇱 Poland | 🇨🇿 Czech Republic
🇵🇹 Portugal | 🇮🇪 Ireland | 🇬🇷 Greece | 🇸🇰 Slovakia | 🇨🇦 Canada | 🇦🇺 Australia

💬 DM me now and let’s talk business! 📩"""

async def send_messages():
    client = TelegramClient('session_name', API_ID, API_HASH)
    try:
        await client.connect()
        
        if not await client.is_user_authorized():
            print("❌ Файл сесії не працює. Авторизація через номер телефону...")
            await client.send_code_request(PHONE_NUMBER)
            code = input("Введіть код, який прийшов на Telegram: ")
            await client.sign_in(PHONE_NUMBER, code)
            print("✅ Авторизація успішна!")

        # Розсилка повідомлень
        for group in GROUPS:
            try:
                await client.send_message(group, MESSAGE)
                print(f"✅ Відправлено в {group}")
                await asyncio.sleep(30)  # Збільшений інтервал
            except errors.FloodWaitError as e:
                print(f"⏳ Зачекайте {e.seconds} секунд...")
                await asyncio.sleep(e.seconds)
                continue
            except errors.PeerIdInvalidError:
                print(f"🚨 Група {group} не знайдена або недоступна")
            except Exception as e:
                print(f"🚨 Помилка: {str(e)}")

    except Exception as e:
        print(f"🔥 Критична помилка: {str(e)}")
    finally:
        await client.disconnect()

async def main():
    max_iterations = 5  # Максимальна кількість ітерацій
    for i in range(max_iterations):
        await send_messages()
        print(f"⏳ Наступна розсилка через 1 годину... (Ітерація {i + 1}/{max_iterations})")
        await asyncio.sleep(3600)

if __name__ == '__main__':
    print("🚀 Запуск розсильника...")
    asyncio.run(main())