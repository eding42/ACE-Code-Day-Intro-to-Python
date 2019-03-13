# Python has a random module for doing things such as
# selecting random items from a list or generating
# random numbers.
#
# Python also has a bunch of other built-in modules.
# To import a module, type "import module-name". like below.
import random

# random.randint: generate a random integer

random_integer = random.randint(1, 10)
print(random_integer)

# random.choice: select a random item from a list
random_item = random.choice(["Fortnite", "Apex", "Anthem"])
print(random_item)

# random.shuffle: shuffles a sequence
x = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(x)
print(x)
