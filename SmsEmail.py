import pyrebase
from config import Config, sender_id, api_key
import requests

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

def send_sms(api_key, sender_id, phone_number, message):
    url = "https://www.fast2sms.com/dev/bulk"

    payload = {
        "sender_id": sender_id,
        "message": message,
        "language": "english",
        "route": "p",
        "numbers": phone_number,
    }

    headers = {
        "authorization": api_key,
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return "SMS sent successfully"
    else:
        return "Failed to send SMS"
    
api_key = api_key
sender_id = sender_id
phone_number = recent_data['number']
email = recent_data['email']
message = "Emergency !!"

res = send_sms(api_key, sender_id, phone_number, message)
print(res)