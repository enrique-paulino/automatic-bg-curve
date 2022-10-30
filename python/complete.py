from helper import *

def fix_curve(sheet):
    new_sheet = []

    for i in range(len(sheet)):
        row = sheet[i]
        last = sheet[i-1]
        for j in range(len(row)):
            if row[j] == '':
                row[j] += last[j]
        new_sheet.append(row)

    return new_sheet

