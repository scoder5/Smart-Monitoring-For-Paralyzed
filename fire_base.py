import pyrebase
from dht import temp
from time import sleep

config = {
    "apiKey": "AIzaSyB8kocn_vbBnFrWqnPhNgcLv4jf_0VSffw",
    "authDomain": "mjorproject.firebaseapp.com",
    "databaseURL": "https://mjorproject-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "mjorproject",
    "storageBucket": "mjorproject.appspot.com",
    "messagingSenderId": "190239547334",
    "appId": "1:190239547334:web:2e5d0ea8d706278edbdcc7",
    "measurementId": "G-07CRCQB83Y"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()
for i in range(5):
    val = temp()
    db.child("temperature")
    data = {"key": val}
    db.set(data)
    sleep(3)
    print(data)