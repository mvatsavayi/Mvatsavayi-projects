# Mahit V.
#LIght up guessing game
#1-3-18
#Guesses a number from 1 - 20 and will flash lights
import random
import time
import RPi.GPIO as GPIO

def game_over():
    '''MY GAME OVER FUNCTION'''
    print("YOU HAVE LOST YOU LOSER DUCKIE DUCK THAT IS PART OF THE EllUMINATI")
    print("THX FOR PLAYING")
def blink_led(pin):
    for i in range(5):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(pin,GPIO.LOW) 
        time.sleep(.2)
def easter_egg():
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


car_radio = ["21","tom brady is da best"]

GPIO.setmode(GPIO.BCM)

LED_pin_red = 21
LED_pin_green = 22
LED_pin_blue = 23


GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT)
GPIO.setup(LED_pin_blue, GPIO.OUT)


#Title and instructions
print("Light up guessing game")
print("""You have 5 guesses to guess a number from 1 to 20
Too low = Blue light
Too High = Red light
Correct = Green light""")

play_again = "Y"

while play_again == "Y":


    # get a number random 1 to 20
    num = random.randint(1,20)
    # Start a loop
    guesses = 0
    while guesses < 5:

    # Get a guess from the user
        guess = input("GUESS A NUMBER FROM 1 TO 20: ")
        if guess in car_radio:
            easter_egg()
            break        
        guess = int(guess)
        guess += 1
        
        #Check if correct , too low or too high
        if guess == num:
                print("YOU win and you get nothing!!!!! WOW isn't that the best gift ever!!!!!")
                blink_led (LED_pin_green)
                break
               
        elif guess < num:
            print("TOO LOW")
            blink_led (LED_pin_blue)

        else: #TOO HIGH
            print("TOO HIGH")
            blink_led (LED_pin_red)

    else:
        game_over()
    play_again = input("Do you want to play again? Y or N").upper()

print("THX FOR PLAYING")

























                
