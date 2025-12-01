from pyrogram import Client, filters

api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"

with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
    print("Userbot is running...")
    app.run()
