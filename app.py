from flask import Flask, render_template 
app = Flask(__name__)

posts = [
    {
        'author': 'Fortune971114',
        'title': 'Post 1',
        'content': 'This is my first conent',
        'date_posted': 'May, 01, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'content': '2nd conent on this sire',
        'date_posted': 'May, 02, 2023'
    }

    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)
    
@app.route("/about")
def about():
        return render_template("about.html", title="About")