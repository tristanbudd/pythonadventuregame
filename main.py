import time
import csv
import random

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
            print("Loading Game...")
            time.sleep(1)
            print("Loading Level...")
            time.sleep(1)
            print("Loading Characters...")
            time.sleep(1)
            verifyFiles()
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
        print(
            "What would you like your starting difficulty to be?\n1 ) Easy - Start With 500 Gold, 3 Lives\n2 ) Medium - Start With 250 Gold, 2 Lives\n3 ) Hard - Start With 0 Gold, 1 Lives")
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
    for i in range(y - 1):
        for l in range(x - 1):
            array[i][l] = " "
    for i in range(1):
        for l in range(x):
            array[i][l] = "#"
    for i in range(y):
        for l in range(1):
            array[i][l] = "#"
    array[1][1] = "Y"
    while 1:
        a = random.randrange(1,9)
        b = random.randrange(1,24)
        if array[a][b] == " ":
            array[a][b] = "B"
            break
    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c)
        csvWriter.writerows(array)
    for i in range(y):
        for l in range(x):
            print(array[i][l], end="")
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
    print("Loading Game...")
    time.sleep(1)
    print("Loading Level...")
    time.sleep(1)
    print("Loading Characters...")
    time.sleep(1)
    verifyFiles()


def verifyFiles():
    a = "charactername="
    b = "gold="
    c = "lives="
    with open(r"data.txt", "r+") as f:
        fileContent = f.read()
        if a in fileContent:
            if b in fileContent:
                if c in fileContent:
                    play()
    print("Invalid Savegame, Returning to main menu...")
    f.close()
    time.sleep(1)
    main()


def play():
    f = open("data.txt", "rt")
    x = 25
    y = 10
    array = [[0] * x for _ in range(y)]

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    charactername = "Error"
    gold = ""
    lives = ""

    while 1:
        f = open("data.txt", "rt")
        with open("map.csv", "r") as c:
            reader = csv.reader(c)
            array = [row for row in reader]
            for i in range(y):
                for l in range(x):
                    print(array[i][l], end="")
                    if l == 24:
                        print()

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
        print("Enter A Character To Interact: W - Up, A - Left, S - Down, D - Right, Q - Quit")
        while 1:
            maininput = input("> ")
            if maininput.upper() == "W":
                moveUp()
            elif maininput.upper() == "A":
                moveLeft()
            elif maininput.upper() == "S":
                moveDown()
            elif maininput.upper() == "D":
                moveRight()
            elif maininput.upper() == "Q":
                print("Returning to Main Menu.")
                time.sleep(0.5)
                print("Returning to Main Menu..")
                time.sleep(0.5)
                print("Returning to Main Menu...")
                time.sleep(0.5)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                main()
            else:
                print("Invalid Input ;(, Please Try Again")

def moveRight():
    x = 25
    y = 10
    array = [[0] * x for _ in range(y)]
    findingArray = []

    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]

    for i in range(len(array)):
        for l in range(len(array[i])):
            if array[i][l] == "Y":
                findingArray.append(i)
                findingArray.append(l)

    if array[findingArray[0]][findingArray[1] + 1] == "#":
        print("Hitting Map Border, Cancelling Move & Refreshing Screen")
        time.sleep(1)
        play()
    if array[findingArray[0]][findingArray[1] + 1] == "B":
        print("Entering The Bar!")
        time.sleep(1)
        bar()

    array[findingArray[0]][findingArray[1]] = " "
    array[findingArray[0]][findingArray[1] + 1] = "Y"

    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    play()


def moveLeft():
    x = 25
    y = 10
    array = [[0] * x for _ in range(y)]
    findingArray = []

    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]

    for i in range(len(array)):
        for l in range(len(array[i])):
            if array[i][l] == "Y":
                findingArray.append(i)
                findingArray.append(l)

    if array[findingArray[0]][findingArray[1] - 1] == "#":
        print("Hitting Map Border, Cancelling Move & Refreshing Screen")
        time.sleep(1)
        play()
    if array[findingArray[0]][findingArray[1] - 1] == "B":
        print("Entering The Bar!")
        time.sleep(1)
        bar()

    array[findingArray[0]][findingArray[1]] = " "
    array[findingArray[0]][findingArray[1] - 1] = "Y"

    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    play()


def moveUp():
    x = 25
    y = 10
    array = [[0] * x for _ in range(y)]
    findingArray = []

    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]

    for i in range(len(array)):
        for l in range(len(array[i])):
            if array[i][l] == "Y":
                findingArray.append(i)
                findingArray.append(l)

    if array[findingArray[0] - 1][findingArray[1]] == "#":
        print("Hitting Map Border, Cancelling Move & Refreshing Screen")
        time.sleep(1)
        play()
    if array[findingArray[0] - 1][findingArray[1]] == "B":
        print("Entering The Bar!")
        time.sleep(1)
        bar()

    array[findingArray[0]][findingArray[1]] = " "
    array[findingArray[0] - 1][findingArray[1]] = "Y"

    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    play()


def moveDown():
    x = 25
    y = 10
    array = [[0] * x for _ in range(y)]
    findingArray = []

    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]

    for i in range(len(array)):
        for l in range(len(array[i])):
            if array[i][l] == "Y":
                findingArray.append(i)
                findingArray.append(l)

    if array[findingArray[0] + 1][findingArray[1]] == "#":
        print("Hitting Map Border, Cancelling Move & Refreshing Screen")
        time.sleep(1)
        play()
    if array[findingArray[0] + 1][findingArray[1]] == "B":
        print("Entering The Bar!")
        time.sleep(1)
        bar()

    array[findingArray[0]][findingArray[1]] = " "
    array[findingArray[0] + 1][findingArray[1]] = "Y"

    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    play()


def bar():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
    f.close()

    print("""
████████╗██╗░░██╗███████╗        ██████╗░░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔════╝        ██╔══██╗██╔══██╗██╔══██╗
░░░██║░░░███████║█████╗░░        ██████╦╝███████║██████╔╝
░░░██║░░░██╔══██║██╔══╝░░        ██╔══██╗██╔══██║██╔══██╗
░░░██║░░░██║░░██║███████╗        ██████╦╝██║░░██║██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝        ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")

    while 1:
        print("\n\n\nWelcome to the bar,", charactername, "Please select an option:\n1 - Gamble, 2 - Exit | Gold:", gold)
        input1 = input("> ")
        if input1 == "1":
            print("Please enter the amount you would like to gamble, Must be below 250 and above 50")
            while 1:
                input2 = int(input("> "))
                if input2 < 250:
                    if input2 > 50:
                        break
                print("Invalid Input, Please follow the games rules.")
            print("Please enter either: 1 - Heads or 2 - Tails")
            while 1:
                input3 = input("> ")
                if input3 == "1":
                    coin = "true"
                    break
                elif input3 == "2":
                    coin = "false"
                    break
                else:
                    print("Invalid Input, Please follow the games rules.")
            print("-", input2, " gold.")
            gold - input2
            print("Flipping Coin.")
            time.sleep(1)
            print("Flipping Coin..")
            time.sleep(1)
            print("Flipping Coin...")
            result = random.randrange(1,100)
            time.sleep(1)
            if result > 50:
                print("The Result Was: Heads!")
                if coin == "true":
                    print("Congratulations, you have doubled your money!")
                    print("+", input2 * 2, "gold.")
                    gold + input2 * 2
                else:
                    print("Sorry, you have lost the money that you have bet.")
            elif result < 50:
                print("The Result Was: Tails!")
                if coin == "false":
                    print("Congratulations, you have doubled your money!")
                    print("+ ", input2 * 2, "gold.")
                    gold + input2 * 2
                else:
                    print("Sorry, you have lost the money that you have bet.")
            else:
                print("It was a draw!, Your money was refunded.")
                print("+ ", input2, " gold.")
                gold + input2

        elif input1 == "2":
            f.close()
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
            print("Data Saved, Returning To Main Game")
            time.sleep(1)
            play()
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNot Found, Please Try Again")

if __name__ == "__main__":
    main()
