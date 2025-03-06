from telethon import TelegramClient
import asyncio

# Дані з my.telegram.org
api_id = '20139205'  # Заміни на свій API ID
api_hash = 'fab8db9897ed148dbb4da62e77621ff4'  # Заміни на свій API Hash
phone_number = '+380634398931'  # Заміни на свій номер телефону

# Список груп (можна використовувати username або ID)
groups = ['@Crypto_Affiliate_eng', '@fortraffic']  # Заміни на свої групи

# Повідомлення для розсилки
message = """🎯  PREMIUM LIVE LEADS 

🚀 Get high-quality, real-time leads that bring results! I work with a wide range of geos and offer flexible deals to fit your needs. Whether you want high-intent traffic or exclusive leads, I can help you scale!

🌍 Top geos available:

🇩🇪 Germany
🇫🇷 France
🇮🇹 Italy
🇪🇸 Spain
🇳🇱 Netherlands
🇸🇪 Sweden
🇳🇴 Norway
🇩🇰 Denmark
🇨🇭 Switzerland
🇬🇧 United Kingdom
🇧🇪 Belgium
🇦🇹 Austria
🇫🇮 Finland
🇵🇱 Poland
🇨🇿 Czech Republic
🇵🇹 Portugal
🇮🇪 Ireland
🇬🇷 Greece
🇸🇰 Slovakia
🇨🇦 Canada
🇦🇺 Australia

💬 DM me now and let’s talk business! 💰📩"""

# Функція для розсилки повідомлень
async def send_messages():
    # Підключення до твого акаунта
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone=phone_number)

    # Розсилка повідомлень у групи
    for group in groups:
        try:
            await client.send_message(group, message)
            print(f"Повідомлення відправлено у групу: {group}")
        except Exception as e:
            print(f"Помилка при відправці в групу {group}: {e}")

    await client.disconnect()

# Запуск розсилки раз на годину
async def main():
    while True:
        await send_messages()
        await asyncio.sleep(3600)  # Затримка на 1 годину (3600 секунд)

# Запуск програми
if __name__ == '__main__':
    asyncio.run(main())from telethon import TelegramClient
import asyncio

# Дані з my.telegram.org
api_id = '20139205'  # Заміни на свій API ID
api_hash = 'fab8db9897ed148dbb4da62e77621ff4'  # Заміни на свій API Hash
phone_number = '+380634398931'  # Заміни на свій номер телефону

# Список груп (можна використовувати username або ID)
groups = ['@Crypto_Affiliate_eng', '@fortraffic']  # Заміни на свої групи

# Повідомлення для розсилки
message = """🎯  PREMIUM LIVE LEADS 

🚀 Get high-quality, real-time leads that bring results! I work with a wide range of geos and offer flexible deals to fit your needs. Whether you want high-intent traffic or exclusive leads, I can help you scale!

🌍 Top geos available:

🇩🇪 Germany
🇫🇷 France
🇮🇹 Italy
🇪🇸 Spain
🇳🇱 Netherlands
🇸🇪 Sweden
🇳🇴 Norway
🇩🇰 Denmark
🇨🇭 Switzerland
🇬🇧 United Kingdom
🇧🇪 Belgium
🇦🇹 Austria
🇫🇮 Finland
🇵🇱 Poland
🇨🇿 Czech Republic
🇵🇹 Portugal
🇮🇪 Ireland
🇬🇷 Greece
🇸🇰 Slovakia
🇨🇦 Canada
🇦🇺 Australia

💬 DM me now and let’s talk business! 💰📩"""

# Функція для розсилки повідомлень
async def send_messages():
    # Підключення до твого акаунта
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone=phone_number)

    # Розсилка повідомлень у групи
    for group in groups:
        try:
            await client.send_message(group, message)
            print(f"Повідомлення відправлено у групу: {group}")
        except Exception as e:
            print(f"Помилка при відправці в групу {group}: {e}")

    await client.disconnect()

# Запуск розсилки раз на годину
async def main():
    while True:
        await send_messages()
        await asyncio.sleep(3600)  # Затримка на 1 годину (3600 секунд)

# Запуск програми
if __name__ == '__main__':
    asyncio.run(main())