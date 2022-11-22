import time
import keyboard
import csv

def main():
    while 1:
        tmp = open("data.txt", "a")
        tmp.close()
        tmp = open("map.csv", "a")
        tmp.close()
        f = open("data.txt", "rt")
        print("""
╔╦═╦╦╦══════╦╦════════╦╦═════╦╦╗
║║║╠╝╠╦╦═╦═╦╣╠╦╗╔╦═╦═╗║║╔═╦═╦╝║║
║║╩║║║║║╩╣║╠╗╔╣╚╝║╠╣╩╣║╚╬╝║║║║║║
║╚╩╩═╩═╩═╩╩╝╚═╩══╩╝╚═╝╚═╩═╩╩╩═╝║
╚══════════════════════════════╝
""")
        if f.read(14) == "charactername=":
            charactername = f.readline()
            charactername.replace('charactername=', '')
            print("Welcome back", charactername.strip("\n"), ", Please select an option:")
        else:
            print("Welcome, Please select an option:")
        f.close()
        print("1 ) Start A New Game")
        print("2 ) Load A Game")
        print("3 ) Settings")
        print("4 ) Quit Game")

        input1 = input("> ")
        if input1 == "1":
            newgame()
        elif input1 == "2":
            maingame()
        elif input1 == "3":
            print("WIP")
        elif input1 == "4":
            exit()
        else:
            print("Invalid Input, Please Try Again.")

def newgame():
    x = 25
    y = 10
    array = [[0] * x for _ in range(y)]
    print("What would you like to call your character?")
    input1 = input("> ")
    while 1:
        print("What would you like your starting difficulty to be?\n1 ) Easy - Start With 500 Gold, 3 Lives\n2 ) Medium - Start With 250 Gold, 2 Lives\n3 ) Hard - Start With 0 Gold, 1 Lives")
        input2 = input("> ")
        if input2 == "1":
            gold = 500
            lives = 3
            break
        elif input2 == "2":
            gold = 250
            lives = 2
            break
        elif input2 == "3":
            gold = 0
            lives = 1
            break
        else:
            print("Invalid Input, Please Try Again.")
    print("Generating The Level...")
    for i in range(y):
        for l in range(x):
            array[i][l] = "#"
    for i in range(y-1):
        for l in range(x-1):
            array[i][l] = " "
    for i in range(1):
        for l in range(x):
            array[i][l] = "#"
    for i in range(y):
        for l in range(1):
            array[i][l] = "#"
    array[1][1] = "Y"
    with open("map.csv", "w+") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    c = open('map.csv', 'r')
    datareader = csv.reader(c, delimiter=';')
    for row in datareader:
        array.append(row)
    for i in range(y):
        for l in range(x):
            print(array[i][l], end= "")
            if l == 24:
                print()
    time.sleep(1)
    print("Saving Level To Data...")
    f = open("data.txt", "w")
    f.write("charactername=")
    f.write(input1)
    f.write("\n")
    f.write("gold=")
    f.write('%d' % gold)
    f.write("\n")
    f.write("lives=")
    f.write('%d' % lives)
    f.write("\n")
    f.close()

    time.sleep(1)
    maingame()

def maingame():
    print("Loading Game...")
    time.sleep(1)
    print("Loading Level...")
    time.sleep(1)
    print("Loading Characters...")
    time.sleep(1)
    f = open("data.txt", "rt")
    if f.read(14) != "charactername=":
        print("Invalid Savegame, Returning to main menu...")
        f.close()
        time.sleep(1)
        main()
    print("Loaded Successfully...")
    f.close()

    play()

def play():
    f = open("data.txt", "rt")
    x = 25
    y = 10
    array = [[0] * x for _ in range(y)]

    charactername = "Error"
    gold = ""
    lives = ""

    while 1:
        charactername = "Error"
        f = open("data.txt", "rt")

        if f.read(14) == "charactername=":
            charactername = f.readline()
            charactername.strip("charactername=")

        f.seek(0)
        for i, line in enumerate(f):
            if i == 1:
                gold = line.strip()
                gold = gold.strip("gold=")
                gold = gold.strip("\n")
                gold = int(gold)

        f.seek(0)
        for i, line in enumerate(f):
            if i == 2:
                lives = line.strip()
                lives = lives.strip("lives=")
                lives = lives.strip("\n")
                lives = int(lives)

        print("Character Name -", charactername.strip("\n"), " Gold -", gold, " Lives -", lives)
        while 1:
            keyboard.on_press_key("left arrow", lambda _: print("Attempting To Move Left"))
            keyboard.on_press_key("right arrow", lambda _: print("Attempting To Move Right"))
            keyboard.on_press_key("up arrow", lambda _: print("Attempting To Move Up"))
            keyboard.on_press_key("down arrow", lambda _: print("Attempting To Move Down"))
            while 1:
                continue

if __name__ == "__main__":
    main()
