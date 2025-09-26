import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API key
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except AttributeError:
    print("Error! API key not found")
    exit()

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])

# Flask app
app = Flask(__name__)

# Serve HTML
@app.route("/")
def index():
    return render_template("index.html")

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat_endpoint():
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    try:
        response = chat.send_message(user_input, stream=True)
        full_text = "".join([chunk.text for chunk in response])
        return jsonify({"reply": full_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
