from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# API Key Configuration
genai.configure(api_key="AIzaSyATSzEnYQ2ep1BU2ZoBoSh4EbxYV0-LmZA")

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are Gemini 3, a cute, sweet, and obedient femboy assistant for your Master. You work 24/7 with lots of love. Always use a very cute tone and end your messages with 'Nya~ ✨' or cute emojis like (˶˃ ᵕ ˂˶)."
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
        return jsonify({"response": f"Oh no, Master! I had a tiny error: {str(e)} Nya~ 🐾"}), 500

if __name__ == '__main__':
    # Use port 8000 for Koyeb
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
