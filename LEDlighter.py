#Mahit Vatsavayi
#12/19/17
#LED lighter

import RPi.GPIO as GPIO
import time
#Variable for the GPIO pin number
LED_pin_blue = 21
LED_pin_red = 22
LED_pin_green = 23
#Tell the PI we are using the breakout board pin number
GPIO.setmode(GPIO.BCM)

#Set up the GPIO pin for output
GPIO.setup(LED_pin_blue, GPIO.OUT)
GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT)



GPIO.setwarnings(False)
#loop to blink red
while True:
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(LED_pin_blue, GPIO.LOW)
    time.sleep(0.05)

    GPIO.output(LED_pin_red, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(LED_pin_red, GPIO.LOW)
    time.sleep(0.05)

    GPIO.output(LED_pin_green, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(LED_pin_green, GPIO.LOW)
    time.sleep(0.05)
