"""
KaiMarkov v1.0.
This is a Markov chain generator which pulls words from
a dataset of Kai's Slack messages. It selects a word randomly
and completes a sentence based on that.
"""
import csv
import random
import os

class MarkovKai:
    def __init__(self):
        self.words = self.getWords()

    def index(self, db="data/dataset.csv"):
        f = open(db)
        reader = csv.reader(f, delimiter=',', quotechar='"')
        f.close()

    def getWords(self, db="data/dataset.csv"):
        """
        Get all the words in the dataset.
        Note that this only runs fast because our dataset is small;
        Larger datasets may take significantly longer (O(n)).
        This can probably be improved.
        """
        words = []
        f = open(db)
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            words.extend([i for i in row[-1].split() if not bool(set(["<"]) & set(i))])
        f.close()

        return words

    def complete(self, word):
        """
        Blindly completes a word based on the words list.
        Note that it makes no distinction between concatenated messages;
        e.g. It will link "in" and "eh" together if they are separate messages.
        """
        indices = [c for c, i in enumerate(self.words) if i == word]

        while len(self.words)-1 in indices:
            indices.remove(len(self.words)-1)

        return self.words[random.choice(indices)+1]

    def chooseRandom(self):
        return random.choice(self.words)



kai = MarkovKai()

def genString(length, word):
    string = ""
    string += word + " "
    for i in range(length):
        word = kai.complete(word)
        string += kai.complete(word) + " "

    return string


if __name__ == "__main__":
    # Set the word to predict on (comment second line to set)

    # startString = "kalyan"
    startString = random.choice(kai.words)

    # Set length (in words)
    strlen = 100

    print(genString(strlen,startString))