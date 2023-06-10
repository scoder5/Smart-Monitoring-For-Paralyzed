# IMPORTS
from flask import Flask, render_template, redirect, redirect, session, url_for, request, Response
import pyrebase
import requests
import cv2
from config import Config
from dht import temp
from testMAX30100 import pulse_oximeter
from acc import Acc

# Flask
app = Flask(__name__)

# Firebase Credentials
apiKey = Config["apiKey"]
authDomain = Config["authDomain"]
databaseURL = Config["databaseURL"]
projectId = Config["projectId"]
storageBucket = Config["storageBucket"]
messagingSenderId = Config["messagingSenderId"]
appId = Config["appId"]
measurementId = Config["measurementId"]


# OpenCV
def generate_frames():
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    camera.release()


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()
app.secret_key = "secret"


@app.route("/")
def home():
    return render_template("/examples/index.html")


@app.route("/dashboard")
def dashboard():
    if 'logged_in' in session and session['logged_in']:
        res = temp()
        Data = Acc()
        oxygen = pulse_oximeter()
        return render_template("/examples/dashboard.html",  temperature=res, oxygen=oxygen, Data=Data)
    else:
        return redirect(url_for('login'))



@app.route("/live")
def live():
    if 'logged_in' in session and session['logged_in']:
        return render_template("/examples/live_monitoring.html")
    else:
        return redirect(url_for('login'))
    
    

@app.route("/emotion")
def emotion():
    if 'logged_in' in session and session['logged_in']:
        return render_template("/examples/emotion.html")
    else:
        return redirect(url_for('login'))
    


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')    



@app.route("/notifications")
def notifications():
    if 'logged_in' in session and session['logged_in']:
        return render_template("/examples/notifications.html")
    else:
        return redirect(url_for('login'))


@app.route("/custom", methods=["GET", "POST"])
def custom():
    if 'logged_in' in session and session['logged_in']:
        if request.method == "POST":
            first = request.form["first"]
            second = request.form["second"]

            data = {
                'first': first,
                'second': second
            }

            db.child('users').push(data)

            return redirect(url_for('dashboard'))

        return render_template("/examples/custom.html")
    else:
        return redirect(url_for('login'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        number = request.form['number']

        data = {
            'number': number,
            'email': email
        }

        db.child('PhoneNumbers').push(data)

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['logged_in'] = True
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

    return render_template('/examples/login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.105", port=8080)
