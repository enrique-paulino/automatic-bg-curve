from helper import *

hero_sheet = read_csv("sheets/hero.csv")[4:90]

def get_info(hero_name):
    for row in hero_sheet:
        if hero_name in row[1]:
            return row

def get_curves(hero_info):
    return [hero_info[10], hero_info[11]]