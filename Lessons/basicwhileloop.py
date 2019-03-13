# 'while' loops are a type of loop in Python
#
# Syntax
#   while(condition):
#
# This runs the indented code a certain amount of times, until the condition is satisfied.
# Unlike 'for' loops, the while loop does not keep track of how many times the loop has been run.
#
# Because of this reason, while loops are simple to understand, but become very unwieldy when coding for larger problems.


# Let's print "hello world" a set number of times:
# Must first declare variable to control the loop.
# Remember, the Python number system starts at 0, not 1.
x = 0

# Now, how many times do we want to run the script?
# let's run it
while(x<12):
    print("hello world")
    x = x+1
    # Remember, you must advance the variable, or the while loop becomes infinite and melts your computer.

# Voila! As we expected, the while loop ran the print statement a total of 12 times.