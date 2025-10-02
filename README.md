# AI Chatbot with Gemini

This project is an AI-powered chatbot built using Google’s Gemini API.
It supports natural language conversations, maintains conversational memory, and includes prompt optimization techniques.
The code is fully hosted on GitHub and demonstrates practical applications of AI, API integration, and version control.

## Features
- Conversational AI using Gemini API
- Persistent memory across interactions
- Optimized prompt handling for accurate responses

## Setup Instructions

1. Clone the repository
```
git clone https://github.com/RyanGaoo/Ryan-Gao-Chat-Bot.git
cd Ryan-Gao-Chat-Bot
```

2. Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up your Gemini 2.0 Flash API key
- Create a `.env` file in the project root
- Add your API key:
```
GEMINI_API_KEY=your_api_key_here
```

5. Run the chatbot
```
python app.py
```

6. Interact with the chatbot via the command line or the hosted interface.

## Contributing
Pull requests are welcome! Please follow standard GitHub best practices.
