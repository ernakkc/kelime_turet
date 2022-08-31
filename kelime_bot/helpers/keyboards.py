from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

keyboard_anlatiyor = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝖾 𝖡𝖺𝗄 👀", callback_data="bak")
    ],
    [
        InlineKeyboardButton("𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝗂 𝖣𝖾𝗀𝗂𝗌 ✏️", callback_data="degis")
    ],
    [
        InlineKeyboardButton("𝖲𝗎𝗇𝗎𝖼𝗎 𝖮𝗅𝗆𝖺𝗄 𝖨𝗌𝗍𝖾𝗆𝗂𝗒𝗈𝗋𝗎𝗆 ⛔", callback_data="istemiyorum")
    ]
])

keyboard_bildi = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("𝖡𝖾𝗇 𝖲𝗎𝗇𝗎𝖼𝗎 𝖮𝗅𝗆𝖺𝗄 𝖨𝗌𝗍𝗂𝗒𝗈𝗋𝗎𝗆 ✋🏻", callback_data="ben")
    ]
])

keyboard_priv_start = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🎉  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  🎉", url=f"http://t.me/KelimeGramBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇹🇷 𝖮𝗐𝗇𝖾𝗋 ", url="t.me/sherlock_exe")
    ],
    [
        InlineKeyboardButton("📝 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋 " , url="t.me/asdasdasdas")
    ]
])
