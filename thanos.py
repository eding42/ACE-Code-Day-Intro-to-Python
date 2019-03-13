import random
# A Thanos Snap simulator
# This thanos script takes a list of people and snaps them randomly - hopefully

# Creates a normanl list of normal people.

people = ["Vincent", "Edward", "Fortnite", "Chungus", "T-Series"]

# Delete half the people
# Deletes one person len(people)//2 times
for i in range(len(people)//2):
    #Select a random person
    snapped = str(random.choice(people))

    # Snap the person
    print("\n" + snapped + " has been snapped.")
    people.remove(snapped)

# Print remaining
print("\nThe people reminaing are: " + str(people))

print("\nSmile... for even in death, you will have become children of Thanos!")