from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    logo_url = url_for('static', filename='flask-logo.svg')
    
    return f"""
    <h1>Welcome to my Flask App!</h1>
    <p>Hello Flask Framework!</p>
    
    <p>Check out the <a href="https://flask.palletsprojects.com/en/stable/quickstart/">Flask Quickstart Guide</a>.</p>
    
    <p>Here is the local Flask logo:</p>
    <img src="{logo_url}" alt="Flask Logo" width="200">
    """

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