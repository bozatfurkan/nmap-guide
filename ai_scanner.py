import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("HATA: API Anahtarı bulunamadı!")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

print("Yapay Zeka Güvenlik Taraması Başlıyor...")

try:
    with open("README.md", "r", encoding="utf-8") as f:
        kod_icerigi = f.read()
        
    prompt = f"Sen kıdemli bir siber güvenlik uzmanısın. Aşağıdaki proje dosyasını incele ve içinde yanlışlıkla unutulmuş şifre, API anahtarı veya güvenlik zafiyeti var mı kontrol et. İçerik:\n\n{kod_icerigi}"
    
    response = model.generate_content(prompt)
    print("\n--- YAPAY ZEKA TARAMA RAPORU ---")
    print(response.text)
    print("--------------------------------")
    
except Exception as e:
    print(f"Tarama sırasında hata oluştu: {e}")
