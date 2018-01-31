#dj mahit in the house
#MAHIT VATSAVAYI
#1/16/2018
#a dj dock

#import needed libraries

import RPi.GPIO as GPIO
import time
import random
import os

#Returns a list of mp3 sound files for the path given
def get_MP3_sounds(sound_path):
    sound_files = os.listdir(sound_path)
    sound_files = [sound_file for sound_file in sound_files
                             if sound_file.endswith(".mp3")]
    return sound_files

#Plays a random sound from the list of mp3 for the given path
def play_random_sound(sound_path, sound_files):
    sound_file = random.choice(sound_files)
    os.system("omxplayer -o local '" + sound_path + "/" + sound_file + "' &")


# Main program
path_music = "/usr/share/scratch/Media/Sounds/Music Loops/"
path_vocals = "/usr/share/scratch/Media/Sounds/Vocals/"
path_effects = "/usr/share/scratch/Media/Sounds/Effects/"

sounds_music = get_MP3_sounds(path_music)
sounds_vocals = get_MP3_sounds(path_vocals)
sounds_effects = get_MP3_sounds(path_effects)





#variables for buttons
button_pin1 = 6
button_pin2 = 19

#set pin numbering
GPIO.setmode(GPIO.BCM)

#setup GPIO for input
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)




#creating two lists with the files in the folders

sounds_music = os.listdir(path_music)
sounds_vocals = os.listdir(path_vocals)

print(sounds_music)
print(sounds_vocals)

sounds_music = [sound for sound in sounds_music if sound.endswith('.mp3')]
sounds_vocals = [sound for sound in sounds_vocals if sound.endswith('.mp3')]
os.system("clear")

title = """
    DJ AWESOME SENSATION
    PRESS ONE FOR MUSIC
    PRESS TWO FOR VOCALS
    PRESS CRTL + C TO EXIT"""

print(title)

while True:
    if GPIO.input(button_pin1):
        print("YOU PRESSED ONE BUTTON")
        play_random_sound(path_music, sounds_music)
        time.sleep(0.1)
    elif GPIO.input(button_pin2):
        print("YOU PRESSED TWO BUTTON")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(0.1)
    elif GPIO.input(button_pin2) and GPIO.input(button_pin2):
        print("easter egg time")
        play_random_sound(path_effect, sounds_effect)
        time.sleep(0.1)
    time.sleep(0.1)

    



