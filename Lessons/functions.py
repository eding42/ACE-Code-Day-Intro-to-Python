# Sometimes, when you're coding, you're lazy and don't want to type
# the same lines of code multiple times.
# The solution to this is functions! It makes a nice machine that
# runs your code with the values you want.
# Example.

# Bad, ugly code:
print("Hi Thanos!")
print("Thanos lives on Titan.")
print("Hi Edward!")
print("Edward lives on Earth.")
print("Hi javaman!")
print("Javaman lives on a trash heap.")

print() # Newline

# The better solution:
def say_hi(name, location):
    print("Hi " + name + "!")
    print(name + " lives on " + location)

say_hi("Thanos", "Titan")
say_hi("Edward", "Earth")
say_hi("Javaman", "a trash heap")

print() # Newline

# See? Much easier to type and read.
# Functions, at their core, take values in, do something with
# it, and spit something (or nothing) out.
# Sound familiar? They're function machines. You do them in 5th grade and you'll
# still be doing them in 10th grade CPM sucks pls end my misery
#
# The function above doesn't output anything. This function outputs a number.

def square(num):
    return num*num

squared = square(4)
print(squared) # Prints 16 
