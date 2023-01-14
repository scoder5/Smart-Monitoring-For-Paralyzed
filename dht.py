import RPi.GPIO as GPIO
import dht11

GPIO.setmode(GPIO.BCM)

def temp():
    while True:
        dht = dht11.DHT11(pin=17)
        result = dht.read()
        if result.is_valid():
            return result.temperature