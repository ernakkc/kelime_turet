from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import keyboard_priv_start

@Client.on_message(filters.command("start") & filters.private)
async def priv_strt(c:Client,m:Message):
    text = f"""**
📖 Merhaba {m.from_user.mention} 

• Ben Bir Kelime Bulma Oyun Botuyum 🎮 

• Çeşitli oyunlar oynamak ve eğlenceli vakit geçirmek için benimle oynayabilirsin ✍🏻 

• Benimle oynamak için beni bir gruba ekleyip yönetici yapman lazim . 💭  
    **"""

    await c.send_message(m.chat.id, text, reply_markup=keyboard_priv_start)

