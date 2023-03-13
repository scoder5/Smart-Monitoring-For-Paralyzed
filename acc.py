from mpu6050 import mpu6050
import time
import RPi.GPIO as GPIO

import smbus
GPIO.setmode(GPIO.BCM)
# Open the I2C bus on bus 4

mpu = mpu6050(0x68,4)

while True:
    print("Temp : "+str(mpu.get_temp()))
    print()

    accel_data = mpu.get_accel_data()
    print("Acc X : "+str(accel_data['x']))
    print("Acc Y : "+str(accel_data['y']))
    print("Acc Z : "+str(accel_data['z']))
    print()
    x = accel_data['x']
    y = accel_data['y']
    z = accel_data['z']
    
    if x > 0 and y > 0 and z > 0:
        print("Output: 1")
    elif x > 0 and y > 0 and z < 0:
        print("Output: 2")
    elif x > 0 and y < 0 and z > 0:
        print("Output: 3")
    elif x < 0 and y > 0 and z > 0:
        print("Output: 4")
    else:
        print("No Output")

    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str(gyro_data['x']))
    print("Gyro Y : "+str(gyro_data['y']))
    print("Gyro Z : "+str(gyro_data['z']))
    print()
    x1 = gyro_data['x']
    y1= gyro_data['y']
    z1 = gyro_data['z']
    
    if x1 > 0 and y1 > 0 and z1 > 0:
        print("G: 1")
    elif x1 > 0 and y1 > 0 and z1 < 0:
        print("G: 2")
    elif x1 > 0 and y1 < 0 and z1 > 0:
        print("G: 3")
    elif x1 < 0 and y1 > 0 and z1 > 0:
        print("G: 4")
    else:
        print("No GOutput")
    print("-------------------------------")
    time.sleep(3)