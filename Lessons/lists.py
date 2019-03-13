# Lists are a list of variables. (woah, who would have guessed?)
# Python lists can store any type of variable.
# You can access them via list[x] where x is the index (starts from 0).

# Create a new list (note the square brackets and commas)
people = ["t-series", "java man", "thanos", "memelord"]
print(people)

# You can access an element (variable) to the list using list[x]
print(people[0]) # Prints t-series, the 0th index/element

# You can add a new element (variable) to the list using append
people.append("edward ding")
print(people)

# You can remove an element by using remove
people.remove("java man")
print(people)

#------ ADVANCED SECTION --------#
# You can slice a part of a list by using list[x:y]
print(people[1:3]) # Prints the people from index 1 (thanos) to 2 (edward ding)
# Note that this stops BEFORE index 3.

# You can iterate/loop through (that is, go through each element of the list)
# using a for loop
# ^^ is this too advanced?
for person in people:
    print(person + " is hella lit my dude.")
