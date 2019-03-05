#!/usr/bin/python3

import datetime
import time
import os

from threading import Thread

now = str(datetime.datetime.now())

now = now[:-7]

print("What is your name\n")

name = input()

if name[-1] == " ":
    name = name[:-1]

elif name.lower() == "edward" or name.lower() == "edward ding":
    name = "Edward Ding"
answer = None


def check():
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
