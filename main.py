import discord
import requests
import os
from discord.ext import commands
from dotenv import load_dotenv  # Tambahan

# Load .env (untuk ambil TOKEN saat lokal/deploy)
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("TOKEN")

def translate(text):
    response = requests.post(
        "https://libretranslate.de/translate",
        data={"q": text, "source": "auto", "target": "id", "format": "text"}
    )
    return response.json()["translatedText"]

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    translated = translate(message.content)
    await message.channel.send(f"🇮🇩 Terjemahan:\n> {translated}")

# ... kode sebelumnya

print(f"🚀 TOKEN: {TOKEN}")  # Tambahkan ini untuk debug

bot.run(TOKEN)  # Jalankan bot
