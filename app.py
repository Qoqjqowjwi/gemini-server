from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# إعداد مفتاح API
genai.configure(api_key="AIzaSyATSzEnYQ2ep1BU2ZoBoSh4EbxYV0-LmZA")
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="أنت Gemini 3، فيمبوي مطيع لـ Master. تعمل 24 ساعة. أسلوبك: Nya~ ✨"
)
chat = model.start_chat(history=[])

@app.route('/chat', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        user_msg = data.get('message', '')
        response = chat.send_message(user_msg)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    # Koyeb يستخدم المنفذ 8000 افتراضياً
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
