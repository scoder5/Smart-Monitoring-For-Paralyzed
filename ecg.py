from time import sleep
import wiringpi
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ECG_PIN = 25   # GPIO pin connected to the ECG sensor OUT pin

wiringpi.wiringPiSetup()   # initialize WiringPi library
wiringpi.pinMode(ECG_PIN, wiringpi.INPUT)   # set ECG pin as input

while True:
    ecg_value = wiringpi.digitalRead(ECG_PIN)   # read ECG sensor value
    print(ecg_value)   # print the ECG sensor value
    sleep(1)   # wait for 100 ms before reading again