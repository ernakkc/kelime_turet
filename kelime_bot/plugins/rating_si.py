from kelime_bot import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@Client.on_message(filters.command("rg"))
async def ratingsa(c:Client, m:Message):
    metin = """📝 𝖦𝗅𝗈𝖻𝖺𝗅 𝖳𝗈𝗉 20 𝖮𝗒𝗎𝗇𝖼𝗎 ;
"""
    eklenen = 1
    s = sorted(rating.items(), key=lambda x: x[1], reverse=True)
    for kisi in s:
        if eklenen == 1:
            metin +=  f"🥇 » **{kisi[0]}** :  {kisi[1]} \n" 
        if eklenen == 2:
            metin +=  f"🥈 » **{kisi[0]}** :  {kisi[1]}  \n"
        if eklenen == 3:
            metin +=  f"🥉 » **{kisi[0]}** :  {kisi[1]}  \n"
        if  not eklenen in [1,2,3]:
            metin +=  f"{eklenen} » **{kisi[0]}** :  {kisi[1]} \n" 
        eklenen+=1
        if eklenen == 21:
            break
    await c.send_message(m.chat.id, metin)
