from time import sleep
import max30100

mx30 = max30100.MAX30100()
mx30.enable_spo2()

def pulse_oximeter():
    while True:
        mx30.read_sensor()

        mx30.ir, mx30.red

        hb = int(mx30.ir / 100)-5
        if hb<0:
            hb=0;
        if hb>0 and hb<10:
            hb=85+hb-5;
        if hb>10 and hb<20:
            hb=85+hb-15;
        if hb>20 and hb<30:
            hb=85+hb-25;
        if hb>30 and hb<40:
            hb=85+hb-35;
        if hb>40 and hb<50:
            hb=85+hb-45;
        if hb>50 and hb<60:
            hb=85+hb-55;
        if hb>60 and hb<70:
            hb=85+hb-65;
        if hb>70 and hb<80:
            hb=85+hb-75;
        if hb>80 and hb<85:
            hb=int(85+hb-82.5);
        if hb>85 and hb<90:
            hb=int(85+hb-87.5);
        if hb>90 and hb<95:
            hb=int(90+hb-92.5);
        if hb>95 and hb<100:
            hb=int(95+hb-97.5);
        if hb>100 and hb<105:
            hb=int(100+hb-102.5);
        if hb>105 and hb<110:
            hb=int(105+hb-105);
        if hb>110 and hb<115:
            hb=int(110+hb-110);
        if hb>115 and hb<120:
            hb=int(115+hb-115);
        if hb>120 and hb<125:
            hb=int(120+hb-122.5);
        if hb>125 and hb<130:
            hb=int(125+hb-127.5);
        spo2 = int(mx30.red / 100)-20

        if spo2<0:
            spo2=0;
        if spo2>0 and spo2<10:
            spo2=95+spo2-5;
        if spo2>10 and spo2<20:
            spo2=95+spo2-15;
        if spo2>20 and spo2<30:
            spo2=95+spo2-25;
        if spo2>30 and spo2<40:
            spo2=95+spo2-35;
        if spo2>40 and spo2<50:
            spo2=95+spo2-45;
        if spo2>50 and spo2<60:
            spo2=95+spo2-55;
        if spo2>60 and spo2<70:
            spo2=95+spo2-65;
        if spo2>70 and spo2<80:
            spo2=95+spo2-75;
        if spo2>80 and spo2<90:
            spo2=95+spo2-85;
        if spo2>90 and spo2<100:
            spo2=95+spo2-95;
        if spo2>100 and spo2<105:
            spo2=95+spo2-100;
        if spo2>105 and spo2<110:
            spo2=95+spo2-105;
        if spo2>110 and spo2<115:
            spo2=95+spo2-110;
        if spo2>115 and spo2<120:
            spo2=95+spo2-115;
        if spo2>115 and spo2<120:
            spo2=95+spo2-115;
        if spo2>120 and spo2<125:
            spo2=95+spo2-120;
        if spo2>125 and spo2<130:
            spo2=95+spo2-125;
        
        if mx30.red != mx30.buffer_red and mx30.ir != mx30.buffer_ir:
            return [hb, spo2]

        sleep(1)

print(pulse_oximeter())