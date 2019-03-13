# Thanos Snap Simulator: Racist edition
# This thanos snapper snaps everyone based on what
# programming language they use
# It uses dictionaries to store the race of the person.

people = {"vincent": "python3",
          "edward": "python2",
          "t-series": "java",
          "ryan": "pascal",
          "memelord": "java"}

# Make a list of people who survived (currently empty)
after_snap = {}

to_snap = "java"

for name, lang in people.items():
    # Go through (name, language) for every person in the dictionary
    # If lang is not the one to be snapped, spare the person
    if lang != to_snap:
        after_snap[name] = lang

# Print survivors
print(after_snap)
