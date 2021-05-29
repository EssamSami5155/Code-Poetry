# Importing necessary modules
import time
import pyttsx3
import os
import itertools


# Setting up a few properties
ROOT_DIR = os.getcwd()
POEM_DIR = ROOT_DIR + "\\poems"
os.chdir(POEM_DIR)
FILES_LIST = os.listdir()
speaker = pyttsx3.init()
speaker.setProperty("rate",150)


# An important function
def print_speak(msg, newline=True):
    if not newline:
        print(msg, end="")
    else:
        print(msg)
    speaker.say(msg)
    speaker.runAndWait()


# Pre Tasks
msg = "Hey there!\n"
print_speak(msg)

msg = "Choose a poem from below:"
print_speak(msg)

time.sleep(0.4)

num = itertools.count()
for poem in FILES_LIST:
    print("Poem " + str(next(num)) + ": " + poem[:-4])
    time.sleep(0.1)

msg = "Input the poem number: "
print_speak(msg, newline=False)
POEM_NUM = input()


# Main Tasks
while True:
    print("\n")
    FILE_NAME = FILES_LIST[int(POEM_NUM)]
    temp = POEM_NUM
    with open(FILE_NAME, "r") as rfile:
        content = rfile.read()
        line_list = content.split("\n")
        for line in line_list:
            print(line)
            speaker.say(line)
            speaker.runAndWait()
        
        print("\n")
        time.sleep(2)
    
    msg = "Input 'n' if you want to hear the next poem"
    print_speak(msg)
    msg = "Input 'a' if you want to quit"
    print_speak(msg)
    
    msg = "Input the poem number: "
    print_speak(msg, newline=False)
    POEM_NUM = input().lower()

    if POEM_NUM == "n":
        POEM_NUM = (int(temp) + 1) % len(FILES_LIST)

    if POEM_NUM == "a":
        break


# Post Tasks
print("\n")

time.sleep(2)
msg = "Thanks for listening."
print_speak(msg)

msg = "Created by Essam Sami & Ahammad Shawki"
print_speak(msg)
time.sleep(3)