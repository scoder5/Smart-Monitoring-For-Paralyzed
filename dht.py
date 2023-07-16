import RPi.GPIO as GPIO
import dht11
# from time import sleep
import pyrebase
from config import Config
from SmsEmail import email_alert, email

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

GPIO.setmode(GPIO.BCM)

def temp():
    while True:
        dht = dht11.DHT11(pin=17)
        result = dht.read()
        if result.is_valid():
            if 36.5 < result.temperature < 37.5:
                email_alert("Emergency", "Critical Alert", email)
            return result.temperature
