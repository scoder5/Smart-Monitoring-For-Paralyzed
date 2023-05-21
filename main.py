from flask import Flask, render_template, redirect, url_for, request, redirect, session
from dht import temp
from testMAX30100 import pulse_oximeter
import pyrebase
import requests

app = Flask(__name__)

Config = {
    "apiKey": "AIzaSyB8kocn_vbBnFrWqnPhNgcLv4jf_0VSffw",
    "authDomain": "mjorproject.firebaseapp.com",
    "databaseURL": "https://mjorproject-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "mjorproject",
    "storageBucket": "mjorproject.appspot.com",
    "messagingSenderId": "190239547334",
    "appId": "1:190239547334:web:2e5d0ea8d706278edbdcc7",
    "measurementId": "G-07CRCQB83Y"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    res = temp()
    return render_template("/examples/dashboard.html",  temperature=res, oxygen=pulse_oximeter())


@app.route("/notifications")
def notifications():
    return render_template("/examples/notifications.html")


@app.route("/icons")
def icons():
    return render_template("/examples/icons.html")


@app.route("/custom")
def custom():
    return render_template("/examples/custom.html")


@app.route("/signup")
def signup():
    return render_template("/examples/signup.html")


@app.route("/login")
def login():
    return render_template("/examples/login.html")


if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.105", port=8080)