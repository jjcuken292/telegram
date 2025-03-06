import asyncio
import schedule
from pyrogram import Client
import time
import os

# Get environment variables with defaults if they are not set
api_id = int(os.getenv("API_ID", "20139205"))  # Default value if not set
api_hash = os.getenv("API_HASH", "fab8db9897ed148dbb4da62e77621ff4")  # Default value if not set
session_name = "my_account"

# Split groups properly by comma
groups = os.getenv("GROUPS", "@dark_side_affiliate_offers,@affiliate_marketing_hub,@delta_fx_crypto_board").split(",")  # Expecting comma-separated group names
message_text = os.getenv("MESSAGE_TEXT", """🎯  PREMIUM LIVE LEADS

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

💬 DM me now and let’s talk business! 💰📩""")

async def send_messages():
    async with Client(session_name, api_id, api_hash) as app:
        for group in groups:
            try:
                await app.send_message(group.strip(), message_text)  # Strip to remove leading/trailing spaces
                print(f"✅ Message sent to {group}")
            except Exception as e:
                print(f"❌ Error sending message to {group}: {e}")

def job():
    asyncio.run(send_messages())

# Schedule the job to run every hour
schedule.every(1).hours.do(job)

print("Text me")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(61)  # Sleep 61 seconds to avoid overloading the scheduler
