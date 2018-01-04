from flask import Flask

app = Flask(__name__)

@app.route('/')
def about():
    return "About content goes here"
def home():
    return "Webpage content goes here"


if __name__ == "__main__":
    app.run(debug = True)
