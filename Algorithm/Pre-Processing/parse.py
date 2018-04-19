# parse the CSV file the program Acceleration generates.

import csv
import math
def parse(data_file):
    acc_data = list()
    with open(data_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # Note the delimiter the program uses
        for row in reader:
            if row[1] == "acc":
                d = float(row[2])**2 + float(row[3])**2 + float(row[4])**2
                d = math.sqrt(d)
                acc_data.append({"d" : d, "time": int(row[0])})
    return acc_data

