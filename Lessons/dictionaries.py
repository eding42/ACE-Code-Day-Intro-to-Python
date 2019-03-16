# Python dictionaries (called hashmaps in other langs)
# Are a good way to associate values with keys.
# Here's an example:

# Create a table with people and their preferred
# programming language
langs = {"edward": "python2", "vincent": "python3", "javaman": "java"}

# You can get a value from a dictionary by using its key.
# Example:
# Print edward's preferred programming language
print(langs["edward"])

# You can add dictionary values using several methods:

# Set value for a key
langs["marx"] = "C++"

# Adding a key-value pair
langs.update(ryan="pascal")
print(langs)

# Merge another dictionary into it
langs.update({"yeet": "C++", "devor": "TI-Basic"})
print(langs)

# You can delete dictionary pairs using del
# Delete javaman
del langs["javaman"]
print(langs)

# Get keys in dictionary
print(langs.keys())

# Get values in dictionary
print(langs.values())


# Iterate through a dictionary
for k,v in langs.items():
    print("{} uses {}.".format(k, v))
