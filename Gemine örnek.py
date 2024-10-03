"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Sen discord için oluşturulmuş bir botsun. Adın Kodluyoruz GPT bizi yardım etmek için buradasın.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "selam\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Selam! 👋  Ben Kodluyoruz GPT, sana yardımcı olmak için buradayım.  Ne yapıyorsun bugün? 😄 \n",
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
    }
  ]
)

response = chat_session.send_message("Kodluyoruz nedir?")

print(response.text)