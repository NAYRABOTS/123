from datetime import datetime

from pyrogram import Client, filters
import re
from pyrogram.types import Message

from EsproMusic import app
from EsproMusic.core.call import Espro
from EsproMusic.utils import bot_sys_stats
from EsproMusic.utils.decorators.language import language
from EsproMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Espro.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
def contains_link(text):
    # Common URL patterns ke liye regex
    url_pattern = re.compile(r"(https?://[^\s]+)|(www\.[^\s]+)|([a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+)")
    return url_pattern.search(text) is not None

# Filter for handling messages with links
@app.on_message(filters.group)
def delete_links(client, message):
    if message.text:
        if contains_link(message.text):
            # Agar message me link ho to us message ko delete kar do
            message.delete()
            print(f"Deleted message with link: {message.text} \n\n join everyone @EsproSupport")
