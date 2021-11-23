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

    value = 0
    direction = 1

    for i in range (8):
        delta = 2 ** (8 - i - 1)
        value += delta * direction

        print(i, value, delta, direction)

        num2pins(dac, value)
        time.sleep(0.5)

        direction = -1 if (GPIO.input(comparator) == 0) else 1

    return value 


try:
    GPIO.output(troykaVoltage, 1)
    while True:
        value = adc()
        num2pins(leds, value)
        print(value)
         
        

finally:
    GPIO.cleanup()



