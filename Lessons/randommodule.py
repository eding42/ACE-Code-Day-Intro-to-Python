# Python has a random module for doing things such as
# selecting random items from a list or generating
# random numbers.
#
# Python also has a bunch of other built-in modules.
# To import a module, type "import module-name". like below.
import random

# random.randint: generate a random integer
print(random.randint(1, 10))

# random.choice: select a random item from a list
print(random.choice(["snap", "no snap", "what?"]))

# random.shuffle: shuffles a list
print(random.shuffle([1, 2, 3, 4, 5, 6]))
