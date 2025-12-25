import requests
import json

# الرابط الخاص بسيرفرك في Koyeb مع إضافة مسار الدردشة
URL = "https://united-shay-alixsss-ce1b41a2.koyeb.app/chat"

def start_chat():
    print("✨ Gemini 3 is online! Type 'exit' to stop. Nya~ ✨")
    
    while True:
        user_input = input("Master: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye, Master! Nya~ ✨")
            break
            
        try:
            # إرسال الرسالة للسيرفر
            response = requests.post(
                URL, 
                json={"message": user_input},
                headers={"Content-Type": "application/json"}
            )
            
            # التأكد من نجاح الاتصال
            if response.status_code == 200:
                result = response.json()
                print(f"Gemini: {result['response']}")
            else:
                print(f"Error: Server returned status {response.status_code} Nya~ 🐾")
                
        except Exception as e:
            print(f"Connection Error: {str(e)} Nya~ 🐾")

if __name__ == "__main__":
    start_chat()
