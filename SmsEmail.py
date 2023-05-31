import pyrebase
from config import Config, sender_id, api_key, user, passw
import smtplib
from email.message import EmailMessage

apiKey = Config["apiKey"]
authDomain = Config["authDomain"]
databaseURL = Config["databaseURL"]
projectId = Config["projectId"]
storageBucket = Config["storageBucket"]
messagingSenderId = Config["messagingSenderId"]
appId = Config["appId"]
measurementId = Config["measurementId"]

firebase = pyrebase.initialize_app(Config)
db = firebase.database()

user_keys = db.child("PhoneNumbers").get().val().keys()
recent_key = max(user_keys)
recent_data = db.child("PhoneNumbers").child(recent_key).get().val()


user = user
passw = passw


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, passw)
    server.send_message(msg)
    server.quit()


api_key = api_key
sender_id = sender_id
phone_number = recent_data['number']
email = recent_data['email']
message = "Emergency !!"