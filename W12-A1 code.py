from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Flask Framework!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye Flask Framework!</p>"

if __name__ == "__main__":
    app.run(debug=True)