from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from kelime_bot import *

@app.on_message(filters.command(["kapat",f"kapat@{USERNAME}"]) & ~filters.private & ~filters.channel)
async def bitir(c:Client, m:Message):
    global oyun
    await c.send_message(m.chat.id,f"**📖 Oyun , {m.from_user.mention} \ntarafından Bitirildi.**\n\n✏️ **Yeni oyun başlatmak için** /game **komutunu kullanabilirsiniz .**")
    oyun[m.chat.id] = {}
