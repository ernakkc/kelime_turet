from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from kelime_bot import *
from kelime_bot.helpers.kelimeler import kelimeler

@Client.on_message(filters.command("data") & filters.user(OWNER_ID))
async def data(c:Client, m:Message):
    global oyun
    print(oyun)
    await m.reply(str(oyun))


@Client.on_message(filters.command("kelimesayi") & filters.user(OWNER_ID))
async def ksayi(c:Client, m:Message):
    await m.reply(f"**Sistemde kayıtlı {len(kelimeler)} kelime bulunmakta . . .**")
