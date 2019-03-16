# This is a reference implementation of
# the final project for ACE Code Day.
# This project is designed to incorporate most, if not all,
# of the concepts we taught.
import random

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1/n2

def thanos(people):
    for person in range(len(people)//2):
        snap = random.choice(people)
        people.remove(snap)
    return people

while True:

    operator = input("Enter an operator (add, sub, mult, div, thanos)")

    if operator != thanos:
        # Normal operation
        num1 = input("Enter number 1:")
        num2 = input("Enter number 2:")

        num1 = int(num1)
        num2 = int(num2)

    else:
        # Thanos snap some scrubs

        # Get names
        people = []
        for i in range(5):
            # Ask for 5 names
            person = input("Enter a person: ")
            people.append(person)

        # Thanos snap these noobs
        survivors = thanos(people)
        print("These people survived:")
        print(survivors)
