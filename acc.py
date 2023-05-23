from mpu6050 import mpu6050
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
mpu = mpu6050(0x68, 4)

def Acc():
    while True:
        # print("Temp : "+str(mpu.get_temp()))
        # print()

        accel_data = mpu.get_accel_data()

        x = accel_data['x']+2.1021090576171875
        y = accel_data['y']+1.13006318359375 - 1
        z = accel_data['z']-10.20169327392578

        gyro_data = mpu.get_gyro_data()

        x1 = gyro_data['x']+3.3587786259541983 + 0.2977099236641223
        y1 = gyro_data['y']+0.5114503816793893 + 0.8320610687022901
        z1 = gyro_data['z']+1.900763358778626 + 0.13740458015267176

        # print("Acc X : "+str(x))
        # print("Acc Y : "+str(y))
        # print("Acc Z : "+str(z))
        # print()
        if x > 0 and y > 0 and z > -1.5:
            return "At Rest"
            # print("At rest")
        elif x >= 4 and y <= -2 and z <= -1:
            return "Please call Emergency Services"
            # print("Please call Emergency Services")
        elif (x > 0 or x < 0) and y > 0 and z < 0:
            return "Need Food/Water"
            # print("Need Food/Water")
        else:
            return "At Rest"
            # print("At Rest")

        # sleep(15)

# Acc()