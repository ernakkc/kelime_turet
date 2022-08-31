from pyrogram import Client
from pyrogram.types import CallbackQuery
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot.helpers.keyboards import *
from kelime_bot import *

@Client.on_callback_query()
async def sunucu(c:Client,cq:CallbackQuery):
    global oyun

    if cq.data == "ben":
        await cq.edit_message_reply_markup()
        await c.send_message(cq.message.chat.id,f"**{cq.from_user.mention}\n• Kelimeyi Anlatıyor 📖**",reply_markup=keyboard_anlatiyor)
        kelime = kelime_sec()
        await cq.answer(f"• 𝖸𝖾𝗇𝗂 𝖪𝖾𝗅𝗂𝗆𝖾 :\n{kelime}", show_alert=True)
        oyun[cq.message.chat.id]["kelime"] = kelime
        oyun[cq.message.chat.id]["oyuncu"] = cq.from_user.id
        


    if cq.data == "bak":
        if cq.from_user.id == oyun[cq.message.chat.id]["oyuncu"]:
            await cq.answer(f"     {oyun[cq.message.chat.id]['kelime']}     ", show_alert=True)
        else:
            await cq.answer("𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝗂 𝖲𝖾𝗇 𝖠𝗇𝗅𝖺𝗍𝗆𝗂𝗒𝗈𝗋𝗌𝗎𝗇 ⛔", show_alert=True)

    if cq.data == "degis":
        if cq.from_user.id == oyun[cq.message.chat.id]["oyuncu"]:
            kelime = kelime_sec()
            oyun[cq.message.chat.id]["kelime"] = kelime
            await cq.answer(f"      {kelime}      ", show_alert=True)
        else:
            await cq.answer("𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝗂 𝖲𝖾𝗇 𝖠𝗇𝗅𝖺𝗍𝗆𝗂𝗒𝗈𝗋𝗌𝗎𝗇 ⛔", show_alert=True)

    if cq.data == "istemiyorum":
        if cq.from_user.id == oyun[cq.message.chat.id]["oyuncu"]:
            await cq.answer(f"𝖠𝗇𝗅𝖺𝗌𝗂𝗅𝖽𝗂 .")
            await c.send_message(cq.message.chat.id,f"**{cq.from_user.mention}** \n• **Anlatmak istemiyor 📖**", reply_markup=keyboard_bildi)
            oyun[cq.message.chat.id] = {}
        else:
            await cq.answer("𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝗂 𝖲𝖾𝗇 𝖠𝗇𝗅𝖺𝗍𝗆𝗂𝗒𝗈𝗋𝗌𝗎𝗇 ⛔", show_alert=True)
