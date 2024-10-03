import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

# API anahtarını yapılandır
genai.configure(api_key=api_key)

# Model oluştur ve prompt gönder
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Sıcağın tersi nedir?")

# Yanıtı yazdır
print(response.text)