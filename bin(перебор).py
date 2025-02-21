import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
troykaVoltage = 17
comparator = 4

GPIO.setmode (GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(troykaVoltage, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

def num2pins (pins, value):
    GPIO.output(pins, [int (i) for i in bin(value)[2:].zfill(8)])

def adc():
    for i in range (255):
        num2pins (dac, i)
        time.sleep(0.001)

        if (GPIO.input(comparator) == 0):
            return 1
    return 255

try:
    GPIO.output(troykaVoltage, 1)
    while True:
        print(adc())    
        

finally:
    GPIO.cleanup()



