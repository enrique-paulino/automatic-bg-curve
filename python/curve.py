from helper import *
from complete import fix_curve

curve_sheet = fix_curve(read_csv("../sheets/curves.csv")[4:20])

def get(curve_name):
    for row in curve_sheet:
        if curve_name in row[2]:
            return row[2:10]

def find(curve_number):
    return curve_sheet[curve_number][2:10]

def start(curve_name):
    curve_info = iter(get(curve_name)[1:])
    return curve_info

def all():
    return [row[2] for row in curve_sheet]