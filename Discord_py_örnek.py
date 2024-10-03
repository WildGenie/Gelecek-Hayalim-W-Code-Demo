import os
import discord
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Discord istemcisi oluştur
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı!')

@client.event
async def on_message(message):
    # Botun kendi mesajlarını görmezden gel
    if message.author == client.user:
        return

    # Gelen mesajı geri gönder
    await message.channel.send(message.content)

# Botu çalıştır
client.run(TOKEN)