from pyrogram import Client, filters
from EsproMusic import app


# Command to get the group invite link based on a specific chat ID
@app.on_message(filters.command("glink"))
async def get_invite_link(client, message):
    # Check if the user has provided the group ID
    if len(message.command) < 2:
        await message.reply("Please provide the group ID.")
        return

    group_id = message.command[1]  # Extract the group ID from the command

    try:
        # Generate or get the invite link for the provided group ID
        invite_link = await client.export_chat_invite_link(int(group_id))
        await message.reply(f"Group Invite Link: {invite_link}")
    except Exception as e:
        await message.reply(f"Error generating invite link: {e}")

