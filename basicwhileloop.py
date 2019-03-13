# 'while' loops are a type of loop in Python
#
# Syntax
#   while(condition):
#
# This runs the indented code until the condition is satisfied.
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
    # The variable has to be incremented manually, otherwise the loop will run forever
    # and your computer will melt.
    x = x+1

# Voila! As we expected, the while loop ran the print statement a total of 12 times.
