from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from kelime_bot import USERNAME, oyun, rating
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *

@Client.on_message(filters.command(["kelime",f"kelime@{USERNAME}"]) & ~filters.private & ~filters.channel)
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("✏️ **Zaten şu anda devam eden bir oyun var ! \n✍🏻 Bitirmek için /kapat komutunu kullanın .**")
    else:
        await m.reply(f"📖 **Kelime Oyunu Başladı .\n\n{m.from_user.mention}** \n**✍🏻 Kelimeyi sunuyor .**", reply_markup=keyboard_anlatiyor)
        oyun[m.chat.id] = {"oyuncu":m.from_user.id , "kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
