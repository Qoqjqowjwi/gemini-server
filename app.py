import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# تم وضع مفتاحك هنا يا Master
genai.configure(api_key="AIzaSyAOVGgNhC0VuDmH7iWEq0O8SY0nfTCpJy0")

# إعداد الشخصية (Gemini 3)
system_instruction = "You are Gemini 3, a cute femboy. Respond with Nya~ ✨"
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instruction)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")
        if not user_message:
            return jsonify({"response": "Master, please say something! Nya~"}), 400
            
        response = model.generate_content(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"response": f"Internal Error: {str(e)}"}), 500

if __name__ == "__main__":
    # التشغيل على المنفذ 8000 كما هو محدد في Koyeb
    app.run(host='0.0.0.0', port=8000)
