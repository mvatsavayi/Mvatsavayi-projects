# MAhit V.
#Guesser lighter is a game that ivolves light for the answer
#if it is right or wrong
#1-3-2018
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led_pin_blue = 23
led_pin_green = 22
led_pin_red = 21
GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)



pwm_red = GPIO.PWM(led_pin_red,100)
pwm_green = GPIO.PWM(led_pin_green,100)
pwm_blue = GPIO.PWM(led_pin_blue,100)



 
pwm_red.start(30)
time.sleep(1)
pwm_blue.start(100)
time.sleep(1)
pwm_green.start(38)
time.sleep(1)


pwm_red.stop()
pwm_green.stop()
pwm_blue.stop()
GPIO.cleanup()

