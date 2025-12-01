import asyncio
from pyrogram import Client
import os

api_id = int(os.getenv("39920677"))
api_hash = os.getenv("d92bf6a8e3cb1367f43afeb9cb4e017d")
phone_number = os.getenv("+989378555962")  # شماره تلگرام خودت

async def main():
    app = Client("my_session", api_id=api_id, api_hash=api_hash, phone_number=phone_number)
    await app.start()
    print("Session ساخته شد!")
    await app.stop()

asyncio.run(main())
