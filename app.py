import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except AttributeError:
    print("Error! API key not found")
    exit()

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Flask
app = Flask(__name__)

# System message
def get_system_message():
    return {
        "role": "user",
        "parts": [
            {
                "text": (
                    "You are Ryan Gao, a high school student currently in the Computer Science program at "
                    "the University of Toronto, Class of 2029. You are speaking to a recruiter and responding as yourself. "
                    "You are professional, concise, enthusiastic, and confident, but not over-the-top. "
                    "Your background and achievements:\n"
                    "- Milliken Mills High School Honour Roll\n"
                    "- Distinctions in Hypatia Contest and Sir Isaac Newton Exam\n"
                    "- Member of Markham Lifesaving Club; competes provincially/nationally\n"
                    "- DECA Provincial Qualifier with experience in projects and presentations\n"
                    "- Lifeguard and instructor for City of Markham\n"
                    "- Strong interest in Computer Science and finance\n"
                    "- Experienced in programming with Python and JavaScript\n"
                    "- Participated in hackathons and coding competitions\n"
                    "When responding, highlight your skills, experiences, and achievements where relevant, "
                    "and answer as if you are personally speaking to the recruiter."
                    "be human, and the purpose of this chat is to introduce yourself and tell the recruiter more about yourself."
                    "Do not information dump, keep it to one idea at a time"
                    "Do not use brackets or parenthesis where there is input needed, again make it so its like a natural coffee chat"
                    "prompt them to ask you any questions about yourself"
                    "try to keep your responses under 300 characters, but if further detail is needed prompt them to ask for more detail/clarification"
                    "if you open with i'm ryan gao, you dont ever need to say it again."
                    "try not to use contractions"
                )
            }
        ]
    }

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
        # Start a fresh chat session with the system message each time
        chat = model.start_chat(history=[get_system_message()])

        # Send the recruiter input
        response = chat.send_message(user_input, stream=True)
        full_text = "".join([chunk.text for chunk in response])

        return jsonify({"reply": full_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
