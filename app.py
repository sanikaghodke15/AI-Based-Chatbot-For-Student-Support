from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Options page
@app.route('/options')
def options():
    return render_template('options.html')

# Chat page
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Login page
@app.route('/login')
def login():
    return render_template('login.html')

# Chatbot API
@app.route('/get', methods=['POST'])
def chatbot_response():
    user_input = request.json['message'].lower()

    if "hello" in user_input:
        return jsonify({"reply": "Hello! How can I help you?"})
    
    elif "admission" in user_input:
        return jsonify({"reply": "You can apply online through our website."})

    elif "course" in user_input:
        return jsonify({"reply": "We offer AI, Python, and Web Development."})

    elif "fee" in user_input:
        return jsonify({"reply": "Fees depend on the course. Please contact admin."})
    
    elif "exam" in user_input:
        return jsonify({"reply": "The exam schedule is available on the student portal. Please check the notice section."})
    
    elif "fees of python" in user_input:
        return jsonify({"reply": "The fees for Python course is ₹15,000."})
    
    elif "fees of web development " in user_input:
        return jsonify({"reply": "The fees for Python course is ₹15,000."})
    
    elif "faculty " in user_input:
        return jsonify({"reply": "We have experienced and qualified faculty members."})
    
    elif "timing" in user_input:
        return jsonify({"reply": "College timing is from 9 AM to 4 PM."})
    
    elif "okay thanks" in user_input:
        return jsonify({"reply": " you're WELCOME"})
    

    else:
        return jsonify({"reply": "I didn't understand."})

if __name__ == '__main__':
    app.run(debug=True)