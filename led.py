#!/usr/bin/env python3
import RPi.GPIO as GP
from gpiozero import LED
from time import sleep
import sys

# LED using gpiozero


def start_led(times=1):
    ledTotalLight = times
    ledCount = 0

    ledBin = 17
    led = LED(ledBin)
    
    # Run led many time
    while ledCount < ledTotalLight:
        print("LED On")
        led.on()
        sleep(1)
        print("LED Off")
        led.off()
        sleep(.7)
        ledCount += 1


# LED using GPIO
def start_led(times=1):
    # Set GPIO Mode
    GP.setmode(GP.BCM)
    # set vars
    ledBin = 17
    ledTotalLight = times
    ledCount = 0
    # Setup bin LED bin
    GP.setup(ledBin, GP.OUT)
    # Run led many time
    try:
        while ledCount < ledTotalLight:
            print("LED On")
            GP.output(ledBin, True)
            sleep(1)

            print("LED Off")
            GP.output(ledBin, False)
            sleep(.7)
    
            ledCount += 1
    finally:
        GP.cleanup()

if __name__ == "__main__":
    try:
        times = int(sys.argv[1])
        start_led(times)
    except:
        print("Few arguments given!\nRun: \n python3 led.py <int times>")
        exit(1)
