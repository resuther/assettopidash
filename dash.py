import requests
import json
import time
import RPi.GPIO as GPIO
import math
import time

# example ip
IP = ("http://127.0.0.1:8002/JSON/telemetrypacket")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(15,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)


GPIO.setup(40,GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

digitclr=[0,0,0,0,0,0,1]
digitr=[0,0,0,0,1,0,1]
digitn=[1,1,1,0,1,1,0]
digit0=[1,1,1,1,1,1,0]
digit1=[0,1,1,0,0,0,0]
digit2=[1,1,0,1,1,0,1]
digit3=[1,1,1,1,0,0,1]
digit4=[0,1,1,0,0,1,1]
digit5=[1,0,1,1,0,1,1]
digit6=[1,0,1,1,1,1,1]
digit7=[1,1,1,0,0,0,0]
digit8=[1,1,1,1,1,1,1]
digit9=[1,1,1,0,0,1,1,0]
digit10=[0,0,0,0,1,1,0]
digit11=[0,1,1,0,1,1,0]
idle1=[1,0,0,0,0,0,0]
idle2=[0,1,0,0,0,0,0]
idle3=[0,0,1,0,0,0,0]
idle4=[0,0,0,1,0,0,0]
idle5=[0,0,0,0,1,0,0]
idle6=[0,0,0,0,0,1,0]
start1=[1,0,0,0,0,0,0]
start2=[1,1,0,0,0,0,0]
start3=[1,1,1,0,0,0,0]
start4=[1,1,1,1,0,0,0]
start5=[1,1,1,1,1,0,0]
start6=[1,1,1,1,1,1,0]
off=[0,0,0,0,0,0,0]
gpin=[40,38,37,36,35,33,32]
gpin2=[31,29,26,24,23,22,21]

def paused():
    clear()
    blank_pins()
    while True:
        try:
            response = requests.get((IP), timeout=2)
        except requests.exceptions.Timeout:
            while True:
                #idle()
                #hour_time_display()
                digdisp(digitclr)
                digdisp2(digitclr)
                try:
                    response = requests.get((IP), timeout=0.5)
                except requests.exceptions.Timeout:
                    continue
                except requests.exceptions.ConnectionError:
                    continue
                else:
                    break
        except requests.exceptions.ConnectionError:
            while True:
                #idle()
                #hour_time_display()
                digdisp(digitclr)
                digdisp2(digitclr)
                try:
                    response = requests.get((IP), timeout=0.5)
                except requests.exceptions.Timeout:
                    continue
                else:
                    break
        time.sleep(1)
        try:
            compare = requests.get((IP), timeout=2)
        except requests.exceptions.Timeout:
            while True:
                #idle()
                #hour_time_display()
                digdisp(digitclr)
                digdisp2(digitclr)
                try:
                    compare = requests.get((IP), timeout=0.5)
                except requests.exceptions.Timeout:
                    continue
                except requests.exceptions.ConnectionError:
                    continue
                else:
                    break
        except requests.exceptions.ConnectionError:
            while True:
                #idle()
                #hour_time_display()
                digdisp(digitclr)
                digdisp2(digitclr)
                try:
                    compare = requests.get((IP), timeout=0.5)
                except requests.exceptions.Timeout:
                    continue
                else:
                    break
        r1 = response.json()
        r2 = compare.json()
        if r1 != r2:
            break

def digdisp(digit):
    for x in range (0,7):
        GPIO.output(gpin[x], digitclr[x])
    for x in range (0,7):
        GPIO.output(gpin[x], digit[x])

def digdisp2(digit):
    for x in range (0,7):
        GPIO.output(gpin2[x], digitclr[x])
    for x in range (0,7):
        GPIO.output(gpin2[x], digit[x])

def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100

def blank_pins():
    GPIO.output(3,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(10,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)

def blank_screen():
    digdisp(off)
    digdisp2(off)

def clear():
    digdisp(digitclr)
    digdisp2(digitclr)

def idle():
    digdisp(idle1)
    digdisp2(idle1)
    time.sleep(0.25)
    digdisp(idle2)
    digdisp2(idle2)
    time.sleep(0.2)
    digdisp2(idle3)
    digdisp(idle3)
    time.sleep(0.1)
    digdisp2(idle4)
    digdisp(idle4)
    time.sleep(0.09)
    digdisp(idle5)
    digdisp2(idle5)
    time.sleep(0.1)
    digdisp2(idle6)
    digdisp(idle6)
    time.sleep(0.2)
    
def hour_time_display():
    hour = time.strftime("%I")
    blank_screen()
    if hour == "01":
        digdisp(digit1)
        time.sleep(2)
    if hour == "02":
        digdisp(digit2)
        time.sleep(2)
    if hour == "03":
        digdisp(digit3)
        time.sleep(2)
    if hour == "04":
        digdisp(digit4)
        time.sleep(2)
    if hour == "05":
        digdisp(digit5)
        time.sleep(2)
    if hour == "06":
        digdisp(digit6)
        time.sleep(2)
    if hour == "07":
        digdisp(digit7)
        time.sleep(2)
    if hour == "08":
        digdisp(digit8)
        time.sleep(2)
    if hour == "09":
        digdisp(digit9)
        time.sleep(2)
    if hour == "10":
        digdisp(digit1)
        time.sleep(2)
        digdisp(digit0)
        time.sleep(2)
    if hour == "11":
        digdisp(digit1)
        time.sleep(1.7)
        blank_screen()
        time.sleep(0.5)
        digdisp(digit1)
        time.sleep(1.8)
    if hour == "12":
        digdisp(digit1)
        time.sleep(2)
        digdisp(digit2)
        time.sleep(2)
    blank_screen()
    time.sleep(0.5)
    digdisp(digitclr)
    time.sleep(1.7)
    blank_screen()
    time.sleep(0.5)
    digdisp(digitclr)
    time.sleep(1.8)
    blank_screen()
    time.sleep(0.5)
    min_time_display()

def min_time_display():
    m = time.strftime("%M")
    mi = m[:1]
    digdisp(digitclr)
    if mi == '0':
        digdisp(digit0)
        time.sleep(1.7)
        blank_screen()
        time.sleep(0.5)
        digdisp(digit0)
        time.sleep(.8)
    if mi == '1':
        digdisp(digit1)
        time.sleep(2)
        digdisp(digit0)
        time.sleep(1)
    if mi == '2':
        digdisp(digit2)
        time.sleep(2)
        digdisp(digit0)
        time.sleep(1)
    if mi == '3':
        digdisp(digit3)
        time.sleep(2)
        digdisp(digit0)
        time.sleep(1)
    if mi == '4':
        digdisp(digit4)
        time.sleep(2)
        digdisp(digit0)
        time.sleep(1)
    if mi == '5':
        digdisp(digit5)
        time.sleep(2)
        digdisp(digit0)
        time.sleep(1)
    time.sleep(2)

def starter():
    GPIO.output(10,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(10,GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)

def startdisp():
    digdisp(start1)
    digdisp2(start1)
    time.sleep(0.1)
    digdisp(start2)
    digdisp2(start2)
    time.sleep(0.1)
    digdisp(start3)
    digdisp2(start3)
    time.sleep(0.1)
    digdisp(start4)
    digdisp2(start4)
    time.sleep(0.1)
    digdisp(start5)
    digdisp2(start5)
    time.sleep(0.1)
    digdisp(start6)
    digdisp2(start6)
    time.sleep(0.5)
    digdisp(digit0)
    digdisp2(digit0)
    digdisp(off)
    digdisp2(off)
    time.sleep(0.2)

def revdown():
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(10,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(3,GPIO.HIGH)
    time.sleep(0.09)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(10,GPIO.LOW)
    time.sleep(0.03)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)
    time.sleep(0.03)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)

start = 1
blights = 1
lights = 1
count = 0
oldres = requests.get('https://github.com/resuther/assettopidash/blob/2b9f07ddfa07389a9f409b2875c8eca1bd943184/resources/oldres.json')
compare = requests.get('https://github.com/resuther/assettopidash/blob/2b9f07ddfa07389a9f409b2875c8eca1bd943184/resources/compare.json')

while True:
    try:
        response = requests.get((IP), timeout=2)
    except requests.exceptions.Timeout:
        while True:
            #idle()
            #hour_time_display()
            digdisp(off)
            digdisp2(off)
            try:
                response = requests.get((IP), timeout=0.5)
            except requests.exceptions.Timeout:
                continue
            except requests.exceptions.ConnectionError:
                continue
            else:
                start = 1
                break
    except requests.exceptions.ConnectionError:
        while True:
            #idle()
            #hour_time_display()
            digdisp(off)
            digdisp2(off)
            try:
                response = requests.get((IP), timeout=0.5)
            except requests.exceptions.Timeout:
                continue
            else:
                start = 1
                break
    if start == 1:
        digdisp(digitclr)
        digdisp2(digitclr)
        starter()
        time.sleep(0.2)
        starter()
        time.sleep(0.2)
        starter()
        startdisp()
        start = 0
    brake = response.json()['BrakePercentage']
    gear = response.json()['Gear']
    pos = response.json()['RacePosition']
    lap = response.json()['Lap']
    event = response.json()['TotalLapsInRace']
    flag = response.json()['CurrentFlag']
    t1 = response.json()['TyreTemperatureRearLeft']
    t2 = response.json()['TyreTemperatureRearRight']
    t3 = response.json()['TyreTemperatureFrontLeft']
    t4 = response.json()['TyreTemperatureFrontRight']
    length = response.json()['TrackLength']
    kmh = response.json()['Speed']
    maxspeed = 300
    speed = (kmh) / (maxspeed) * 100
    temp = t1 + t2 + t3 + t4
    avgtemp = (temp / 4)
    if avgtemp > 95:
        GPIO.output(16,GPIO.HIGH)
    if avgtemp < 95:
        GPIO.output(16,GPIO.LOW)
    if flag != 0:
        GPIO.output(18,GPIO.HIGH)
    if flag == 0:
        GPIO.output(18,GPIO.LOW)
    if speed < 1:
        GPIO.output(15,GPIO.LOW)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
    if speed > 2:
        GPIO.output(15,GPIO.LOW)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)
    if speed > 33:
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
    if speed > 66:
        GPIO.output(15,GPIO.LOW)
        GPIO.output(11,GPIO.HIGH)
        GPIO.output(19,GPIO.LOW)
        
#    if event == -1:
#        if lap == 1:
#            digdisp2(digit1)
#        if lap == 2:
#            digdisp2(digit2)
#        if lap == 3:
#            digdisp2(digit3)
#        if lap == 4:
#            digdisp2(digit4)
#        if lap == 5:
#            digdisp2(digit5)
#        if lap == 6:
#            digdisp2(digit6)
#        if lap == 7:
#            digdisp2(digit7)
#        if lap == 8:
#            digdisp2(digit8)
#        if lap == 9:
#            digdisp2(digit9)
#    else:
#        if pos == 1:
#            digdisp2(digit1)
#        if pos == 2:
#            digdisp2(digit2)
#        if pos == 3:
#            digdisp2(digit3)
#        if pos == 4:
#            digdisp2(digit4)
#        if pos == 5:
#            digdisp2(digit5)
#        if pos == 6:
#            digdisp2(digit6)
#        if pos == 7:
#            digdisp2(digit7)
#        if pos == 8:
#            digdisp2(digit8)
#        if pos == 9:
#            digdisp2(digit9)
    if gear == 0:
        digdisp(digitn)
    if gear == 1:
        digdisp(digit1)
    if gear == 2:
        digdisp(digit2)
    if gear == 3:
        digdisp(digit3)
    if gear == 4:
        digdisp(digit4)
    if gear == 5:
        digdisp(digit5)
    if gear == 6:
        digdisp(digit6)
    if gear == 7:
        digdisp(digit7)
    if gear == 8:
        digdisp(digit8)
    if gear == -1:
        digdisp(digitr)
    maxrev = response.json()['MaxRevs']
    rpm = response.json()['EngineRevs']
    if lights == 0:
        if brake > 5:
            GPIO.output(13,GPIO.HIGH)
        if brake < 5:
            GPIO.output(13,GPIO.LOW)
        if brake > 35:
            blights = 1
            GPIO.output(10,GPIO.HIGH)
        if brake > 90:
            blights = 1
            GPIO.output(8,GPIO.HIGH)
            GPIO.output(5,GPIO.HIGH)
        if brake < 35:
            blights = 0
            GPIO.output(10,GPIO.LOW)
        if brake < 90:
            blights = 0
            GPIO.output(8,GPIO.LOW)
            GPIO.output(5,GPIO.LOW)
        
    if 150 < rpm < 1000:
        digdisp2(digit0)
    if 1000 < rpm < 2000:
        digdisp2(digit1)
    if 2000 < rpm < 3000:
        digdisp2(digit2)
    if 3000 < rpm < 4000:
        digdisp2(digit3)
    if 4000 < rpm < 5000:
        digdisp2(digit4)
    if 5000 < rpm < 6000:
        digdisp2(digit5)
    if 6000 < rpm < 7000:
        digdisp2(digit6)
    if 7000 < rpm < 8000:
        digdisp2(digit7)
    if 8000 < rpm < 9000:
        digdisp2(digit8)
    if 9000 < rpm < 10000:
        digdisp2(digit9)
    if maxrev == 0:
        maxrev = 8000
    revper = (rpm) / (maxrev) * 100
    if rpm < 130:
        GPIO.output(3,GPIO.LOW)
        digdisp2(digitclr)
        lights = 1
    if rpm > 130:
        lights = 1
    if revper >= 87:
        lights = 1
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
    if revper < 87:
        lights = 0
        GPIO.output(12,GPIO.LOW)
        GPIO.output(3,GPIO.LOW)
    if revper >= 92:
        lights = 1
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
    if revper < 92:
        if blights == 0:
            lights = 0
            GPIO.output(8,GPIO.LOW)
            GPIO.output(5,GPIO.LOW)
    if revper >= 97:
        lights = 1
        GPIO.output(10,GPIO.HIGH)
    if revper < 97:
        if blights == 0:
            lights = 0
            #GPIO.output(10,GPIO.LOW)
    if revper >= 99:
        g1 = response.json()['Gear']
        lights = 1
        while True:
            response = requests.get((IP))
            g2 = response.json()['Gear']
            maxrev = response.json()['MaxRevs']
            rpm = response.json()['EngineRevs']
            brake = response.json()['BrakePercentage']
            revper = (rpm) / (maxrev) * 100
            GPIO.output(8,GPIO.HIGH)
            GPIO.output(10,GPIO.HIGH)
            GPIO.output(12,GPIO.HIGH)
            GPIO.output(3,GPIO.HIGH)
            GPIO.output(5,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(8,GPIO.LOW)
            GPIO.output(10,GPIO.LOW)
            GPIO.output(12,GPIO.LOW)
            GPIO.output(3,GPIO.LOW)
            GPIO.output(5,GPIO.LOW)
            time.sleep(0.1)
            if brake > 3:
                lights = 0
                break
            if g1 != g2:
                lights = 0
                break
            if revper < 97:
                if g1 == g2:
                    if brake < 20:
                        revdown()
                        lights = 0
                        break
                else:
                    lights = 0
                    break
    count += 1
    if count == 10:
        compare = requests.get(IP)
        r1 = oldres.json()
        r2 = compare.json()
        if r1 == r2:
            paused()
        count = 0
        if count == 0:
            oldres = requests.get((IP))
