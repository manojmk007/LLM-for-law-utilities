from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Common greetings and responses
COMMON_PHRASES = {
    "hello": "Hello! How can I assist you with legal matters?",
    "hi": "Hi there! Ask me about Indian law.",
    "hlo": "Hello! How can I assist you with legal matters?",
    "hey": "Hey! Feel free to ask me legal questions.",
    "how are you": "I'm here to assist you with legal queries!",
    "good morning": "Good morning! What legal help do you need?",
    "good evening": "Good evening! How can I assist you legally?"
}

# Keywords to identify legal queries
LEGAL_KEYWORDS = [
    "act", "law", "legal", "section", "IPC", "contract", "court", "rights",
    "fine", "penalty", "case", "arrest", "FIR", "bail", "justice", "petition",
    "punishment", "lawyer", "judge", "legal procedure", "crime", "process", "procedure ", "warrant"
]

def is_legal_query(user_input):
    """Check if user input is related to law"""
    return any(keyword in user_input.lower() for keyword in LEGAL_KEYWORDS)

def model(prompt):
    """Process user query with Indian_Law_LLM AI"""
    user_input = prompt.lower().strip()

    if user_input in COMMON_PHRASES:
        return COMMON_PHRASES[user_input]
        
    if not is_legal_query(user_input):
        return "I specialize in Indian law. Please ask legal questions."

    try:
        model_name = 'Indian_Law_LLM'  # Your model's name
        try:
            model = genai.GenerativeModel(model_name)
        except:
            model = genai.GenerativeModel('Indian_Law_LLM_pro')  # Fallback to previous model
        
        chat = model.start_chat()
        
        structured_prompt = f"""You are an AI legal assistant for Indian law. 
        Provide responses in this format:
        1. 📜 Relevant Law/Act :
        2. 📖 Explanation :
        3. ⚖️ Legal Procedure :
        
        Question: {prompt}
        """
        
        response = chat.send_message(structured_prompt)
        return response.text.replace("*", "").strip()
        
    except Exception as error:
        logger.error(f"Indian_Law_LLM API Error: {error}")
        return "⚠️ Error processing request. Please try again."

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def get_response():
    user_input = request.form.get('msg', '').strip()
    if not user_input:
        return jsonify({"response": "Please enter a valid question."})
    return jsonify({'response': model(user_input)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
