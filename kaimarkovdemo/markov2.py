"""
Markov v2.0
This version of the Kai Markov generator
is supposed to give a substantial accuracy boost
by taking phrases and tokens into account.
The original KaiMarkov implementation resides in markov.py.
"""
import csv
import random

class KaiMarkov2:
    def __init__(self):
        self.tokens = self.getPhrases()

    def getPhrases(self):
        f = open("data/dataset.csv")
        reader = csv.reader(f, delimiter=',', quotechar='"')
        fulltext = ""
        tokens = {}
        for row in reader:
            fulltext += row[-1] + " "

        fulltext = fulltext.split()

        for c, word in enumerate(fulltext):
            if c >= 2:
                try:
                    tokens[" ".join(fulltext[c-2:c])].append(word)
                except KeyError:
                    tokens[" ".join(fulltext[c-2:c])] = [word]

        return tokens

    def complete(self, token):
        return random.choice(self.tokens[token])


kai = KaiMarkov2()

string = random.choice(list(kai.tokens.keys()))
for i in range(50):
    token = " ".join(string.split()[-2:])
    string += " " + kai.complete(token)

print(string)
