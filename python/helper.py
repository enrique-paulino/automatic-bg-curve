import csv

def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def print_curves(curves):
    for i in range(len(curves)):
        print("(" + str(i+1) + ")" + curves[i].center(25))
    