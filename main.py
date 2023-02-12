from flask import Flask, render_template, redirect, url_for
from dht import temp
from testMAX30100 import pulse_oximeter

app = Flask(__name__)

# config = {
#     "apiKey": "AIzaSyB8kocn_vbBnFrWqnPhNgcLv4jf_0VSffw",
#     "authDomain": "mjorproject.firebaseapp.com",
#     "databaseURL": "https://mjorproject-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "projectId": "mjorproject",
#     "storageBucket": "mjorproject.appspot.com",
#     "messagingSenderId": "190239547334",
#     "appId": "1:190239547334:web:2e5d0ea8d706278edbdcc7",
#     "measurementId": "G-07CRCQB83Y"
# }

# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
# db.child("temperature").push({"value": 30})
# db.child("temperature").update({"value": 30})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    res = temp()
    return render_template("/MajorFE/examples/dashboard.html",  temperature=res, oxygen=pulse_oximeter())

@app.route("/notifications")
def notifications():
    return render_template("/MajorFE/examples/notifications.html")

@app.route("/icons")
def icons():
    return render_template("/MajorFE/examples/icons.html")

@app.route("/user")
def user():
    return render_template("/MajorFE/examples/user.html")

if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.104")
