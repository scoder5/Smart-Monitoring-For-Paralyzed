from mpu6050 import mpu6050
import RPi.GPIO as GPIO
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
mpu = mpu6050(0x68, 4)

def Acc():
    user_keys = db.child("users").get().val().keys()
    recent_key = max(user_keys)
    recent_data = db.child("users").child(recent_key).get().val()

    while True:
        accel_data = mpu.get_accel_data()

        x = accel_data['x']+2.1021090576171875
        y = accel_data['y']+1.13006318359375 - 1
        z = accel_data['z']-10.20169327392578

        gyro_data = mpu.get_gyro_data()

        x1 = gyro_data['x']+3.3587786259541983 + 0.2977099236641223
        y1 = gyro_data['y']+0.5114503816793893 + 0.8320610687022901
        z1 = gyro_data['z']+1.900763358778626 + 0.13740458015267176

        if x > 0 and y > 0 and z > -1.5:
            return "At Rest"
        elif x >= 4 and y <= -2 and z <= -1:
            email_alert("Hey!", recent_data['first'], email)
            return recent_data['first']
        elif (x > 0 or x < 0) and y > 0 and z < 0:
            email_alert("Hey!", recent_data['second'], email)
            return recent_data['second']
        else:
            return "At Rest"