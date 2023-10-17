from helper import *
from complete import fix_curve

curve_sheet = fix_curve(read_csv("../sheets/curves.csv")[4:20])
curve_info = fix_curve(read_csv("../sheets/curves.csv"))


def get(curve_name):
    for row in curve_sheet:
        if curve_name in row[2]:
            note = max(row, key = len)
            return note, row[2:10]

def find(curve_number):
    return curve_sheet[curve_number][2:10]

def start(curve_name):
    _, row = get(curve_name)
    curve_info = iter(row[1:])
    return curve_info

def all():
    return [row[2] for row in curve_sheet]

def note(curve_name):
    note, _ = get(curve_name)
    return note