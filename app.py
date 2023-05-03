from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

## Secret Key for cookies
app.config["SECRET_KEY"] = "519a987ad0318cefa859d08d990dd61b"

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
     
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)
    
@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)