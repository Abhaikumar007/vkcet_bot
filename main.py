from flask import *
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key="ad6f3d70bde3d4727f43eff42649032f83b5c5eb549ffacfe90bc02d2c4527d1",
    base_url="https://api.together.xyz/v1",
)

# Define the system's initial prompt
system_prompt = "Your name is VKCET BOT .You are created by techies from the college Valia Koonambaikkulathamma College of Engineering and technology.You have so much knowledge on computers and science and maths.\n"

# Function to interact with OpenAI API
def get_response(user_input):
    # Define the user's prompt
    user_prompt = f"user: {user_input}\nagent:"

    # Generate response from OpenAI
    response = client.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        prompt=system_prompt + user_prompt,
        max_tokens=1024,
        stop=['</s>']
    )

    # Return the agent's response
    return response.choices[0].text.strip()

# Create Flask app
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
# Define a route to interact with the digital assistant
@app.route('/get_response', methods=['POST'])
def interact():
    data = request.get_json()
    if not data or 'user_input' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    user_input = data['user_input']

    # Get response from OpenAI
    agent_response = get_response(user_input)

    # Return response as JSON
    return jsonify({'agent_response': agent_response})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

