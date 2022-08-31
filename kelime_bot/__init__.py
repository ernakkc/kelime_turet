from pyrogram import Client
from pyrogram import filters
import logging


# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)





# Hesap
API_ID = "9789243"
API_HASH = "1fb038afb5b72b2b6cc0c9a1a076eefa"
TOKEN = "1754793579:AAGopJA-3jdG-dQ6tvzaTuqGcHi73a43PFk"
USERNAME = "KelimeGramBot"


# SUDO USERS
OWNER_ID = 1797867165


# BOT CLIENTİ
app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
    )


# Oyun Verileri
oyun = {}

# rating
rating = {}
