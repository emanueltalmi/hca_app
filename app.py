from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/mealprep/')
def mealprep():
    return render_template("mealprep.html")


@app.route('/groceryorder/')
def groceryorder():
    return render_template("groceryorder.html")


@app.route('/medicalorder/')
def medicalorder():
    return render_template("medicalorder.html")


@app.route('/login/')
def login():
    return render_template("login.html")


@app.route('/signup/')
def signup():
    return render_template("signup.html")
