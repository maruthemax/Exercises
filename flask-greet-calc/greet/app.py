from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    return "welcome home"


@app.route("/welcome/back")
def welcom_back():
    return "welcome back"