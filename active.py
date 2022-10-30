import csv

def get_char():
    char = str(input("Enter a character: "))
    info = []

    with open("sheets/hero.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == char.capitalize():
                info = row

    return info

def get_stats(info):
    name = info[1]
    main_curve = info[10]
    alt_curve = info[11]
    return name , main_curve , alt_curve

def show_stats():
    stats = get_stats(get_char())
    print("*-------------------------*")
    print(stats[0])
    print("Main Curve: " + stats[1])
    print("Alt Curve: " + stats[2])
    print("*-------------------------*")

def main():
    while True:
        show_stats()

main()