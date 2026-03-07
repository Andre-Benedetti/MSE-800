from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    logo_url = url_for('static', filename='flask-logo.svg')
    
    return f"""
   <div style="background-color: green; color: red; min-height: 100vh; padding: 20px; font-family: sans-serif;">
        <h1>Welcome to my Flask App!</h1>
        <p>Hello Flask Framework!</p>
        
        <p>Check out the <a href="https://flask.palletsprojects.com/en/stable/quickstart/" style="color: yellow;">Flask Quickstart Guide</a>.</p>
        
        <hr style="border: 0.5px solid white; margin: 20px 0;">

        <h3>File Browser</h3>
        <p>Use the link below to open the logo file:</p>
        
        <a href="{logo_url}" target="_blank" style="color: #ADFF2F; font-weight: bold; font-size: 1.2em;">
            Browse Image
        </a>

        <br><br>
        
    </div>
    """

@app.route("/bye")
def bye():
    return "<p>Bye Flask Framework!</p>"

@app.route("/username/<name>")
def learner(name):
    return f"{name} is learning FLASK!"

@app.route("/username/<name>/<int:number>")
def learner2(name, number):
    return f"""
    <div style="background-color: green; color: white; min-height: 100vh; padding: 20px; font-family: sans-serif;">
        <h1>Welcome to my Flask App!</h1>
        <p>{name} is learning FLASK!{name} wakes up at {number} a.m. every day</p>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)