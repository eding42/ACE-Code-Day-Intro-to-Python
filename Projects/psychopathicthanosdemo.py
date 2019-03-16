# Thanos Snap Simulator: Class Warfare edition
# This thanos snapper snaps everyone based on what
# socioeconomic class they are. You, like the purge. 
# It uses dictionaries to store the class of the person.

people = {"vincent": "middle class",
          "edward": "middle class",
          "t-series": "filthy rich",
          "pewdiepie": "filthy rich",
          "java man": "peasant"}

# Make a list of people who survived (currently empty)
after_snap = []
snapped = []

to_snap = "middle class"

for name, lang in people.items():
    # Go through (name, language) for every person in the dictionary
    # If lang is not the one to be snapped, spare the person
    if lang != to_snap:
        after_snap.append(name)

    elif lang == to_snap:
        snapped.append(name)

# Print survivors and snapped

# Converts the list into a string, with .join method, separated by a comma.
after_snap = ", ".join(after_snap)
snapped = ", ".join(snapped)

print(after_snap + " have survived\n")

print(snapped + " have been snapped")

