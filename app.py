import os
from pyrogram import Client, filters

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
target_chat = os.getenv("TARGET_CHAT")  # مثلا آیدی چت خودت

app = Client(
    "my_session",
    api_id=api_id,
    api_hash=api_hash
)

# روی پیام‌های کانال
@app.on_message(filters.channel)
async def forward_channel_messages(client, message):
    await client.forward_messages(
        chat_id=target_chat,
        from_chat_id=message.chat.id,
        message_ids=message.id
    )

app.run()
