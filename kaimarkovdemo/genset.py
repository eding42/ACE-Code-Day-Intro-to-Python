"""
genset v. 1.0
Filters out Slack messages to only include Kai's messages.
This way we filter the training data to not include noise
from other humans.
This script also aggregates all data into one CSV file for easy training.
You know, parsing. Fun.
"""
import csv
import os

os.chdir("data/")

tmp = open("dataset.csv", "w", newline="")

for fpath in os.scandir("."):
    if fpath.name.split(".")[-1] == "csv" and fpath.is_file() and fpath.name != "dataset.csv":
        print(fpath.name)


        with open(fpath.name, "r", newline="\n") as f:
            # Create CSV reader and writer
            reader = csv.reader(f, delimiter=',', quotechar='"')
            writer = csv.writer(tmp, delimiter=',', quotechar='"', lineterminator="\n")

            # Add msg to dataset if msg was sent by kai
            for row in reader:
                print(row)
                if row[2] == "kg2084":
                    writer.writerow(row)


tmp.close()
