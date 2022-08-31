from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot import *

@Client.on_message(filters.text & ~filters.private & ~filters.channel )
async def buldu(c:Client, m:Message):
    global oyun
    try:
        if m.chat.id in oyun:
            if m.from_user.id != oyun[m.chat.id]["oyuncu"]:
                if m.text.lower() == oyun[m.chat.id]["kelime"]:
                    await m.reply(f"**{m.from_user.mention} \nKelimeyi buldu ✅** \n**✏️ Kelime :**  `{oyun[m.chat.id]['kelime']}`",reply_markup=keyboard_bildi)
                    oyun[m.chat.id] = {}
            else:
                if m.text.lower() == oyun[m.chat.id]["kelime"]:
                    await m.reply("✏️**Hey dostum ! \n✍🏻 Kelimeyi söylemek yok !**")
                    try:
                        await m.delete()
                    except:
                        pass
    except KeyError:
        pass

         
