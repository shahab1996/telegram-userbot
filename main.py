from pyrogram import Client
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client(
    "userbot_session",
    api_id=API_ID,
    api_hash=API_HASH,
)

@app.on_message()
async def handler(client, message):
    print(message.text)

app.run()
