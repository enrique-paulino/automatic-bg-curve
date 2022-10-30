from helper import *

import os
import hero
import curve

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

def run_curve(curve_turns):
    curve_info = curve.start(curve_turns)
    turn = 0
    while True:
        try:
            turn += 1
            temp = "Turn: " + str(turn)
            print(temp.center(30))
            print("*---------------------------*")
            print(next(curve_info).center(30))
            print("*---------------------------*")
            input("Press Enter to continue...")
            cls()

        except:
            print("End of curve".center(30))
            print("*---------------------------*")
            break

if __name__ == '__main__':
    print("*---------------------------*")
    print("Enter your hero name".center(30))
    print("*---------------------------*")

    choose_hero = str(input(">>> ")).capitalize()
    hero_info = hero.get_info(choose_hero)
    cls()

    print("*---------------------------*")
    print("Select a curve".center(30) + "\n")
    print_curves(hero.get_curves(hero_info))
    print("\n(0)" + "Pick Other".center(25))
    print("*---------------------------*")

    choose_curve = int(input(">>> "))
    cls()

    if choose_curve == 0:
        print("*---------------------------*")
        print("Select a curve".center(30) + "\n")
        all_curves = curve.all()
        print_curves(all_curves)
        print("*---------------------------*")
        new_choice = int(input(">>> "))
        cls()
        run_curve(all_curves[new_choice-1])
        
    elif hero.get_curves(hero_info)[choose_curve-1] == "Special Curve":
        print("*----------------------------------------------*")
        print("Special Curve is an undefined curve".center(50))
        print("that depends on the early".center(50))
        print("minions that you find.\n".center(50))
        print("If you want to pick your own curve,".center(50))
        print("press enter or ctrl + c to exit.".center(50))
        print("*----------------------------------------------*")
        try:
            choice = input(">>> ")
        except KeyboardInterrupt:
            exit()

        cls()
        
        print("*---------------------------*")
        print("Select a curve".center(30) + "\n")
        all_curves = curve.all()
        print_curves(all_curves)
        print("*---------------------------*")
        new_choice = int(input(">>> "))
        cls()
        run_curve(all_curves[new_choice-1])



    else:
        run_curve(hero.get_curves(hero_info)[choose_curve-1])
