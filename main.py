import discord
import os
from discord.ext import commands
from googletrans import Translator

# Inisialisasi bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Ambil TOKEN dari environment variable
TOKEN = os.getenv("TOKEN")

# Translator Google
translator = Translator()

# Fungsi translate
def translate(text):
    result = translator.translate(text, dest='id')
    return result.text

# Event saat bot aktif
@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user}")

# Event saat pesan masuk
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    translated = translate(message.content)
    await message.channel.send(f"🇮🇩 Terjemahan:\n> {translated}")

# Jalankan bot
bot.run(TOKEN)
