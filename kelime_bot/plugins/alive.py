from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from kelime_bot import OWNER_ID




@Client.on_message(filters.command(["botcum", "alive"], [".", "/"]) & filters.user(OWNER_ID))
async def sahip(c: Client, m: Message):
    await m.reply("**ᴍᴇʀʜᴀʙᴀ sᴀʜɪᴘ ʙᴇʏ ✋🏻 \nᴇᴍʀɪɴɪᴢᴅᴇʏɪᴍ 🥳**")
