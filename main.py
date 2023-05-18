from pyrogram import Client, filters


API_ID = "10349117"
API_HASH = "fb88362d7567e017155bcc39d4efa059"
BOT_TOKEN = "5979937723:AAGwJdJktjrxwvcINvMSbaXEmJ1oIOW7Z6k"


KDBOTZZ = Client(
    name="PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Bot Started")

KDBOTZZ.run()
