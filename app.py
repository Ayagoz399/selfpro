from flask import Flask
import random

app = Flask(__name__)

quotes = [
     "discipline beats motivation"
     "small steps every day"
]

@app.route("/")

def home():
    return random.choice(quotes)
app.run(host="0.0.0.0", port=5000)

