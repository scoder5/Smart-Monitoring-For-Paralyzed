from time import sleep
import max30100

mx30 = max30100.MAX30100()
mx30.enable_spo2()

def pulse_oximeter():
    while True:
        mx30.read_sensor()

        mx30.ir, mx30.red

        hb = int(mx30.ir / 100)
        spo2 = int(mx30.red / 100)
        
        if mx30.red != mx30.buffer_red and mx30.ir != mx30.buffer_ir:
            return [hb, spo2]

        sleep(1)

print(pulse_oximeter())