import os
import discord
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Loads in your Discord Bot Token and sets it as a constant. This used to connect the bot to Discord's API.
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# When the bot connects successfully to the Discord API, this prints out a message to say that it has connected.


@client.event
async def on_ready():
    print("Successfully connected as {0.user}".format(client))


@client.event
async def on_message(message):
    # Makes the bot only respond to messages from the user/question asker, not from itself.

    print("mesaj geldi", message.channel.id, CHANNEL_ID, type(message))

    if message.author == client.user:
        return

    # Checks if the bot was mentioned in the message (using @)

    if (
        str(message.channel.id) == CHANNEL_ID
        or message.channel.type == discord.ChannelType.private
    ):  # if client.user in message.mentions:
        # This uses the OpenAI API to generate a response to the question

        async with message.channel.typing():
            response = cevap(message.content, message.author)

        # Sends the response as a message from the bot.

        await message.channel.send(response)


def cevap(message, author):
    # Create the model
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
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
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
                    "Kodluyoruz nedir?",
                ],
            },
            {
                "role": "model",
                "parts": [
                    '"Kodluyoruz" aslında birkaç farklı anlama geliyor, bağlama göre değişebilir.  Aşağıdaki anlamları olabilir:\n\n**1. Topluluk:** "Kodluyoruz" genellikle **teknoloji ve programlama ile ilgilenen bir topluluk** anlamına gelir. Bu topluluk içerisinde bireyler; kodlama öğrenmek, projeler geliştirmek, diğer kişilerle bilgi paylaşımı yapmak ve birbirlerine destek olmak için bir araya gelirler. Bu topluluklar, çeşitli online platformlarda (Discord gibi) veya yüz yüze etkinliklerde (workshoplar, konferanslar gibi) faaliyet gösterebilirler.\n\n**2. Etkinlik:** "Kodluyoruz" ayrıca bir **teknoloji etkinliğinin adı** olabilir. Bu etkinlikler, kodlama, yazılım geliştirme, tasarım, yapay zeka gibi konularda eğitim, atölye çalışmaları, konferanslar ve yarışmalar gibi çeşitli etkinlikler içerebilir. \n\n**3. Proje:** "Kodluyoruz" ayrıca **bir yazılım projesinin adı** olabilir. Bu proje, genellikle topluluk üyeleri tarafından geliştirilen ve genellikle açık kaynaklı olarak paylaşılır.\n\nSizin "Kodluyoruz"dan neyi kastettiğinizi biraz daha ayrıntılı olarak anlatabilir misiniz? Böylece daha spesifik bir cevap verebilirim. 😊\n',
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

    response = chat_session.send_message(
        message
    )  # (f"userid: {author.id}, username:{author.name}, content: {message}")

    return response.text


# This line runs the bot.
client.run(TOKEN)
