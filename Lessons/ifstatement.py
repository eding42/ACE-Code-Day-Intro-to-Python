# This is a demonstration of the if statement in Python.
# If statements are pretty much the most important part of coding
# It enables the computer to make decisions

x = 0
# If variable x has a value of 0, print "x is equal to 0"
if x == 0:
    print("x is equal to 0\n")


java = "bad"
# If variable java has a value of "bad", print "JAVA MAN BAD"
if java == "bad":
    print("JAVA MAN BAD")

# If statements have a few special cases.
# These cases are "elif" and "else".
# "Else" runs a piece of code when none of the other
# statements are true.
# "Elif" is basically shorthand for else: if condition: 

heathen = "python2"

if heathen == "java":
    # If heathen has value "java", print "java man bad"
    print("java man bad")
elif heathen == "python2":
    # If heathen has value "python2", print "python2 is old"
    print("python2 is old")
else:
    # If heathen is not "java" or "python2", print "good"
    print("good")
