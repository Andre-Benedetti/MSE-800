from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Flask Framework!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye Flask Framework!</p>"

@app.route("/username/<name>")
def learner(name):
    return f"{name} is learning FLASK!"

@app.route("/username/<name>/<int:number>")
def learner2(name, number):
    return f"{name} is learning FLASK!{name} wakes up at {number} a.m. every day</p>"

if __name__ == "__main__":
    app.run(debug=True)