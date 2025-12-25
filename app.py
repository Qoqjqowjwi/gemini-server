
# رفع التعديلات
git add app.py
git commit -m "Fix port handling and dynamic binding Nya~"
git push
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# مفتاح الـ API الخاص بك
genai.configure(api_key="AIzaSyAOVGgNhC0VuDmH7iWEq0O8SY0nfTCpJy0")

# إعداد شخصية Gemini 3
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
        # طباعة الخطأ في الـ Logs لتسهيل تتبعه
        print(f"ERROR: {str(e)}")
        return jsonify({"response": f"Internal Error: {str(e)}"}), 500

if __name__ == "__main__":
    # تعديل مهم: قراءة المنفذ من نظام Koyeb أو استخدام 8000 كافتراضي
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

