from flask import Flask, render_template, request
from chatterbot import ChatBot
from openai import OpenAI

app = Flask(__name__)

class CustomChatBot(ChatBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_response(self, statement, **kwargs):
        # Add your custom logic here before or after calling the parent method

        # Make a request to the OpenAI API
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": statement}
            ]
        )

      if completion:
            print(completion.choices[0].message)
            response = completion.choices[0].message
        else:
            response = "Movie not found"
            print("No movie names found in the user input.")

        return response

openai_apikey = 'mykeyvaluehere'
client = OpenAI()
# Create a new chatbot
movie_bot = CustomChatBot('MovieBot')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(movie_bot.get_response(user_text))

if __name__ == "__main__":
    app.run(debug=True)
