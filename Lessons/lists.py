# Lists are a list of variables. (woah, who would have guessed?)
# Python lists can store any type of variable.
# You can access them via list[x] where x is the index (starts from 0).

# Create a new list (note the square brackets and commas)
people = ["t-series", "java man", "thanos"]
print(people)

# You can add a new element (variable) to the list using append
people.append("edward ding")
print(people)

# You can remove an element by using remove
people.remove("java man")
print(people)

# You can iterate/loop through (that is, go through each element of the list)
# using a for loop
# ^^ is this too advanced?
for person in people:
    print(person + " is hella lit my dude.")
