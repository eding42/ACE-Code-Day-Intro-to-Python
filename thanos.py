import random
# A Thanos Snap simulator
# This thanos script takes a list of people and snaps them randomly

# Create list of people
people = ["vincent", "edward", "john cena", "memelord", "t-series"]

# Delete half the people
# Deletes one person len(people)//2 times
for i in range(len(people)//2):
    #Select a random person
    snapped = random.choice(people)

    # Snap the person
    people.remove(snapped)

# Print remaining
print(people)
