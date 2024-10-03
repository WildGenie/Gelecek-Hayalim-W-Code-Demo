import os
import discord
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Loads in your Discord Bot Token and sets it as a constant. This used to connect the bot to Discord's API.
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# When the bot connects successfully to the Discord API, this prints out a message to say that it has connected.

@client.event
async def on_ready():
    print('Successfully connected as {0.user}'.format(client))

@client.event
async def on_message(message):

    print('mesaj geldi',message.channel.id,CHANNEL_ID,type(message))

    if message.author == client.user:
        return

    if str(message.channel.id) == CHANNEL_ID or message.channel.type == discord.ChannelType.private: #if client.user in message.mentions:

        async with message.channel.typing():

            response = cevap(message.content,message.author)

        await message.channel.send(response)

def cevap(message,author):

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 2000,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Merhaba sen bir discord sohbet botusun, Adın Kodluyoruz GPT. Bize bir selamlama gönder. Selamlama gönderirken mention olarak bu kişiyi etiketle <@&134362454976102401>",
    )

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "Selam",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Merhaba! 👋 Ben Kodluyoruz GPT,  sizinle sohbet etmek ve sorularınızı yanıtlamak için buradayım!  <@&134362454976102401>  nasılsınız? 😄 \n",
        ],
        },
        {
            "role": "user",
            "parts": [
                "Kodluyoruz nedir?\n",
            ],
        },
        {
            "role": "model",
            "parts":[
                "Kodluyoruz, Türkiye'de gençleri teknoloji alanında eğiterek iş gücüne katmayı amaçlayan bir sosyal girişimdir. Özellikle yazılım, veri bilimi ve teknolojiye dayalı çeşitli alanlarda eğitim programları düzenler. Kodluyoruz, bu alanlara ilgi duyan gençlere teknik beceriler kazandırarak onları iş dünyasına hazırlar. Eğitimlerde çeşitli seviyelerde programlama dilleri, yazılım geliştirme süreçleri, proje yönetimi ve kariyer koçluğu gibi konular ele alınır. Ayrıca, katılımcılara mentor desteği sağlayarak kariyer gelişimlerine de katkıda bulunur. Misyonları, Türkiye'nin teknoloji ekosistemine yetkin ve donanımlı genç profesyoneller kazandırmaktır."
                ],
        },
        {
        "role": "user",
        "parts": [
            "Merhaba sen bir discord sohbet botusun, Adın Kodluyoruz GPT. Bize bir selamlama gönder. Selamlama gönderirken mention olarak bu kişiyi etiketle <@&134362454976102401>",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Merhaba herkes! Ben Kodluyoruz GPT, sizinle sohbet etmek ve eğlenceli bir deneyim sunmak için buradayım! 👋 \n\n<@&134362454976102401>, özellikle sizinle tanışmak için heyecanlıyım! 🎉 \n\nSizden haber almak ve neler olup bittiğini öğrenmek için sabırsızlanıyorum! \n",
        ],
        },
    ]
    )

    response = chat_session.send_message(message) #(f"userid: {author.id}, username:{author.name}, content: {message}")

    return response.text

client.run(TOKEN)