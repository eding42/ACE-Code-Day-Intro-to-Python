# For loops run a certain amount of times.
# They can also loop through lists (although that is more advanced)

# Construct a new for loop
for i in range(20):
    # Runs 20 times
    print("java man bad")

print() # Newline

#---- Behind the Scenes ----#
# How is this working?
# We can see if we print i:
for i in range(20):
    # Runs 20 times
    print(i)

print() # Newline

# range(20) actually makes a list from 0..19, which the for loop loops through.
# This means that the code runs 20 times - the first time, i = 0,
# the second time, i = 1, etc.
# It's equivalent to this:

i = 0
while i < 20:
    print(i)
    i = i + 1 # or i += 1 if you want to save 2 characters

print() # Newline
#---- Back to Normal Stuff ----#
# For loops can also loop through lists. For example:

people = ["edward ding", "thanos", "lenin", "stalin"]
for person in people:
    print(person + " is hella lit.")

print() # Newline
# That is equivalent to this:

people = ["edward ding", "thanos", "lenin", "stalin"]
x = 0
while x < len(people):
    print(people[x] + " is hella lit.")
    x += 1
