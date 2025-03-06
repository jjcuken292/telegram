python
import asyncio
import schedule
from pyrogram import Client
import time
import os

api_id = int(os.getenv("20139205"))
api_hash = os.getenv("fab8db9897ed148dbb4da62e77621ff4
")
session_name = "my_account"

groups = os.getenv("GROUPS").split("@ark_side_affiliate_offers,@affiliate_marketing_hub,@delta_fx_crypto_board")
message_text = os.getenv("MESSAGE_TEXT", "🎯  PREMIUM LIVE LEADS 

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

💬 DM me now and let’s talk business! 💰📩")

async def send_messages():
    async with Client(session_name, api_id, api_hash) as app:
        for group in groups:
            try:
                await app.send_message(group, message_text)
                print(f"✅ it's ok {group}")
            except Exception as e:
                print(f"❌ error {group}: {e}")

def job():
    asyncio.run(send_messages())

schedule.every(1).hours.do(job)

print("TEXT ME")
while True:
    schedule.run_pending()
    time.sleep(60)
