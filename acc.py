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
 
    x = accel_data['x']+2.1021090576171875;
    y = accel_data['y']+1.13006318359375 -1;
    z = accel_data['z']-10.20169327392578;
    print("Acc X : "+str(x))
    print("Acc Y : "+str(y))
    print("Acc Z : "+str(z))
    print()
    if x > 0 and y > 0 and z >-1.5:
        print("Output: At Rest")
    elif x >= 4 and y <= -2 and z <= -1:
        print("Output: Please call Emergency Services")
    elif (x > 0 or x<0) and y > 0 and z < 0:
        print("Output: Need Food/Water")
    else:
        print("Output: At Rest")

    gyro_data = mpu.get_gyro_data()
    
    x1 = gyro_data['x']+3.3587786259541983 + 0.2977099236641223;
    y1= gyro_data['y']+0.5114503816793893 + 0.8320610687022901;
    z1 = gyro_data['z']+1.900763358778626 + 0.13740458015267176;
    
    # print("Gyro X : "+str(x1))
    # print("Gyro Y : "+str(y1))
    # print("Gyro Z : "+str(z1))
    # print()
    # if x1 < -50 and y1 <= -10 and z1 <0:
    #     print("selected")
        
    # # elif x1 >= 0 and y1 >= 0 and z1 <= 0:
    # #     print("G: 2")
    # # elif x1 >= 0 and y1 <= 0 and z1 >= 0:
    # #     print("G: 3")
    # # elif x1 <= 0 and y1 >= 0 and z1 >= 0:
    # #     print("G: 4")
    # else:
    #   print("Not Selected")
    #   print("-------------------------------")
    time.sleep(3)