from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define the list of patterns and responses
pairs = [
    [r"my name is (.*)", ["Hello %1, How are you today?"]],
    [r"hi|hey|hello", ["Hello!", "Hey there!", "Hi, how can I help you?"]],
    [r"what is your name?", ["I am a chatbot created by you.", "I am your friendly assistant chatbot."]],
    [r"how are you?", ["I'm doing good! How about you?"]],
    [r"sorry (.*)", ["It's okay. Don't worry!", "No worries, friend!"]],
    [r"i'm (.*) doing good", ["Nice to hear that!", "Great, how can I help you today?"]],
    [r"(.*) your age?", ["I'm a computer program, I don't have an age!"]],
    [r"what (.*) want?", ["I'm here to assist you with whatever you need."]],
    [r"(.*) created you?", ["I was created by a Python developer using NLTK.", "I am a Python program, created with NLTK."]],
    [r"(.*) (location|city) ?", ["I am a virtual assistant. I don't have a physical location."]],
    [r"how is weather in (.*)?", ["I don't have access to weather data. Please check online for the weather in %1."]],
    [r"quit", ["Goodbye! Take care.", "It was nice talking to you. See you soon!"]],
]

# Initialize the chatbot with the defined patterns and reflections
chatbot = Chat(pairs, reflections)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the chat page
@app.route('/chat')
def chat():
    return render_template('chat.html')

# API route to handle AJAX requests from the front end
@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot.respond(user_input)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)
