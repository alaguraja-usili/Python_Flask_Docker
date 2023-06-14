from flask import Flask
from markupsafe import Markup
from jinja2 import Markup, escape

app = Flask(__name__)

@app.route("/")
def run():
    return "{\"message\":\"Hey there python\"}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
