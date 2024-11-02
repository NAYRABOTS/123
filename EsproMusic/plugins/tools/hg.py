from pyrogram import Client, filters
from EsproMusic import app

@app.on_message(filters.video_chat_started)
async def video_chat_started(client, message):
    chat = message.chat
    # Get the user who started the video chat
    user = message.from_user
    if user:
        username = user.username if user.username else "No username"
        user_id = user.id
        full_name = f"{user.first_name} {user.last_name if user.last_name else ''}".strip()
        
        # Construct the message
        msg = f"🎥 User {full_name} (ID: {user_id}, Username: @{username}) joined the video chat."
        
        # Send the message to the group
        await app.send_message(chat.id, msg)

@app.on_message(filters.video_chat_ended)
async def video_chat_ended(client, message):
    chat = message.chat
    # Get the user who ended the video chat
    user = message.from_user
    if user:
        username = user.username if user.username else "No username"
        user_id = user.id
        full_name = f"{user.first_name} {user.last_name if user.last_name else ''}".strip()
        
        # Construct the message
        msg = f"❌ User {full_name} (ID: {user_id}, Username: @{username}) ended the video chat."
        
        # Send the message to the group
        await app.send_message(chat.id, msg)

