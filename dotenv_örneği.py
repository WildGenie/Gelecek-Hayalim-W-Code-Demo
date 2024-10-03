from dotenv import load_dotenv
import os

# .env dosyasındaki değişkenleri yükle
load_dotenv()

# Ortam değişkenlerini al
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
DISCORD_CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

# Kullanım örneği
print(f'DISCORD_TOKEN: {DISCORD_TOKEN}')
print(f'GEMINI_API_KEY: {GEMINI_API_KEY}')
print(f'DISCORD_CHANNEL_ID: {DISCORD_CHANNEL_ID}')