import discord
import requests
import os
from discord.ext import commands

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
    print(f"🚀 TOKEN: {TOKEN}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    translated = translate(message.content)
    await message.channel.send(f"🇮🇩 Terjemahan:\n> {translated}")

bot.run(TOKEN)
