# IMPORTS
from flask import Flask, render_template, redirect, request, redirect, session
from dht import temp
from testMAX30100 import pulse_oximeter
import pyrebase
import requests
from config import Config


app = Flask(__name__)

apiKey = Config["apiKey"]
authDomain = Config["authDomain"]
databaseURL = Config["databaseURL"]
projectId = Config["projectId"]
storageBucket = Config["storageBucket"]
messagingSenderId = Config["messagingSenderId"]
appId = Config["appId"]
measurementId = Config["measurementId"]


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()
app.secret_key = "secret"



@app.route("/")
def home():
    return render_template("/examples/index.html")


@app.route("/dashboard")
def dashboard():
    res = temp()
    return render_template("/examples/dashboard.html",  temperature=res, oxygen=pulse_oximeter())


@app.route("/notifications")
def notifications():
    return render_template("/examples/notifications.html")


@app.route("/custom")
def custom():
    return render_template("/examples/custom.html")


@app.route("/signup", methods = ["GET", "POST"])
def signup():

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        if len(password) < 6:
            return "Password should be at least 6 characters!"
        
        try:
            user = auth.create_user_with_email_and_password(email, password)
            if user:
                session['user'] = email
                return redirect('/dashboard')
            else:
                return "User creation failed"
            
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error_message = error_json['error']['message']
            if error_message == "EMAIL_EXISTS":
                return "Email already exists. Please use a different email to sign up."
            else:
                return str(e)


    return render_template("/examples/signup.html")



@app.route("/login", methods = ["GET", "POST"])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            return redirect('/dashboard')
        
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error_message = error_json['error']['message']
            if error_message == "EMAIL_NOT_FOUND":
                return "Email not found. Please check your email and try again."
            elif error_message == "INVALID_PASSWORD":
                return "Invalid password. Please check your password and try again."
            else:
                return str(e)

    return render_template("/examples/login.html")



@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.105", port=8080)