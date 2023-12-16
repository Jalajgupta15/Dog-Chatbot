import json
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load dog breeds data
with open("dog_breeds.json", "r") as file:
    dog_breeds_data = json.load(file)

def get_dog_breed_info(breed_name):
    breed_info = dog_breeds_data.get(breed_name.lower())
    if breed_info:
        return breed_info
    else:
        return None

def generate_bot_response(user_input):
    user_input = user_input.lower()

    if "dog" in user_input and "breed" in user_input:
        return "Sure, I can provide information about dog breeds. Please specify the breed you're interested in."

    breed_info = get_dog_breed_info(user_input)
    if breed_info:
        response = f"{breed_info['name']} is a {breed_info['size']} dog with a {breed_info['temperament']} temperament. " \
                   f"They typically live for {breed_info['lifespan']} years."
    else:
        response = "I'm sorry, I couldn't find information about that dog breed. Please try another one."

    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    bot_response = generate_bot_response(user_message)
    return jsonify({'bot_response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
