from flask import Flask 
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h2>Flask Home Page</h2>";
    
@app.route("/about")
def about():
        return "<h2>The About Page</h2>";