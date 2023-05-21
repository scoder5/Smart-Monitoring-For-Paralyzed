import pyrebase
from dht import temp
from time import sleep
from config import Config

apiKey = Config["apiKey"]
authDomain = Config["authDomain"]
databaseURL = Config["databaseURL"]
projectId = Config["projectId"]
storageBucket = Config["storageBucket"]
messagingSenderId = Config["messagingSenderId"]
appId = Config["appId"]
measurementId = Config["measurementId"]

firebase = pyrebase.initialize_app(Config)
storage = firebase.storage()
db = firebase.database()
for i in range(5):
    val = temp()
    db.child("temperature")
    data = {"key": val}
    db.set(data)
    sleep(3)
    print(data)