#!/usr/bin/python3
#gotta have a shebang line
import datetime
import time
import os
from threading import Thread


# Get the date using builtin datetime module
# Way less hacky than Edward's solution
now = datetime.datetime.now().date()

# Ask the user for their name
name = input("What is your name?:")

# Remove extra spaces from name
name = name.strip()

# Autocorrect name if you're too lazy to type it properly
if name.lower() == "edward" or name.lower() == "edward ding":
    name = "Edward Ding"

# Wait for an input from the user
# If the user doesn't respond say they are dead
def check():
    # Scoping is important edward
    answer = None
    time.sleep(7)
    if answer != None:
        return
    print("too slow lol")
    time.sleep(2)
    result = '\nAs of "{}", {} is dead.\n'.format(now, name)
    file = open("stillalive.txt", "a+")
    file.write(result)
    file.write("")
    print(result)
    time.sleep(1)
    os._exit(0)


Thread(target=check).start()

while True:
    answer = str(input("\nHello {}, are you still alive today? ".format(name)))
    if answer.lower() == "yes" or answer.lower() == "no":
        break

if answer == None:
    os._exit(0)

if answer.lower() == "yes":
    print("\nGood! Now stay that way!\n")

    # if statement below prevents typos from extra spaces

    result = 'As of "{}", {} is still alive.\n'.format(now, name)

    file = open("stillalive.txt", "a+")

    file.write(result)
    file.write("")

    print(result)

if answer.lower() == "no":
    result = '\nAs of "{}", {} is dead.\n'.format(now, name)

    file = open("stillalive.txt", "a+")
    file.write(result)
    file.write("")
    print(result)
