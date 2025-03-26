from telethon.sync import TelegramClient

api_id = 20324969
api_hash = '4fbc4584fab68524bd119766b201d6e6'
phone_number = '+380668721279'

client = TelegramClient('session_name', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))