from telethon.sync import TelegramClient

api_id = 20599035
api_hash = '46964f4cd05ae0609707b0eca16c4c7f'
phone_number = '+380996645372'

client = TelegramClient('session_name', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))