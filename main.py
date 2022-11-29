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
            settings()
        elif input1 == "4":
            exit()
        else:
            print("Invalid Input, Please Try Again.")

def newgame():
    array = [[0] * 25 for _ in range(10)]
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
    for i in range(10):
        for l in range(25):
            array[i][l] = "#"
    for i in range(10 - 1):
        for l in range(25 - 1):
            array[i][l] = " "
    for i in range(1):
        for l in range(25):
            array[i][l] = "#"
    for i in range(10):
        for l in range(1):
            array[i][l] = "#"
    array[1][1] = "Y"
    while 1:
        a = random.randrange(2,8)
        b = random.randrange(2,23)
        if array[a][b] == " ":
            array[a][b] = "B"
            break
    while 1:
        a = random.randrange(2,8)
        b = random.randrange(2,23)
        if array[a][b] == " ":
            array[a][b] = "A"
            break
    while 1:
        a = random.randrange(2,8)
        b = random.randrange(2,23)
        if array[a][b] == " ":
            array[a][b] = "H"
            break
    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c)
        csvWriter.writerows(array)
    for i in range(10):
        for l in range(25):
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
    judgement = 0
    array = [[0] * 25 for _ in range(10)]

    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]

    while 1:
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "Z":
                    judgement = judgement + 1
                    break
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "J":
                    judgement = judgement + 1
                    break
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "F":
                    judgement = judgement + 1
                    break
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "G":
                    judgement = judgement + 1
                    break
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "A":
                    judgement = judgement + 1
                    break
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "S":
                    judgement = judgement + 1
                    break
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "H":
                    judgement = judgement + 1
                    break
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "B":
                    judgement = judgement + 1
                    break

        if judgement <= 0:
            while 1:
                a = random.randrange(2, 8)
                b = random.randrange(2, 23)
                if array[a][b] == " ":
                    array[a][b] = "G"
                    break

        with open("map.csv", "w", newline="") as c:
            csvWriter = csv.writer(c)
            csvWriter.writerows(array)

        break
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    charactername = "Error"
    gold = ""
    lives = ""

    while 1:
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

        if lives <= 0:
            print("""
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─████████──████████─██████████████─██████──██████─████████████████──────████████████───██████████████─██████████████─████████████───────────────────██████─
─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████───────────────████░░██─
─████░░██──██░░████─██░░██████░░██─██░░██──██░░██─██░░████████░░██──────██░░████░░░░██─██░░██████████─██░░██████░░██─██░░████░░░░██────██████───████░░████─
───██░░░░██░░░░██───██░░██──██░░██─██░░██──██░░██─██░░██────██░░██──────██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██──██░░██────██░░██─████░░████───
───████░░░░░░████───██░░██──██░░██─██░░██──██░░██─██░░████████░░██──────██░░██──██░░██─██░░██████████─██░░██████░░██─██░░██──██░░██────██████─██░░████─────
─────████░░████─────██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██───────────██░░██───────
───────██░░██───────██░░██──██░░██─██░░██──██░░██─██░░██████░░████──────██░░██──██░░██─██░░██████████─██░░██████░░██─██░░██──██░░██────██████─██░░████─────
───────██░░██───────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██──██░░██────██░░██─████░░████───
───────██░░██───────██░░██████░░██─██░░██████░░██─██░░██──██░░██████────██░░████░░░░██─██░░██████████─██░░██──██░░██─██░░████░░░░██────██████───████░░████─
───────██░░██───────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░████─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░████───────────────████░░██─
───────██████───────██████████████─██████████████─██████──██████████────████████████───██████████████─██████──██████─████████████───────────────────██████─
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
            print("\nYour character has died, To keep playing you can give yourself lives in the setting menu. Or you can create a new character.")
            print("If you found it difficult, feel free to try playing on a different difficulty.\n")
            time.sleep(5)
            print("1 ) Acknowledge & Return To Main Menu")
            while 1:
                input1 = input("> ")
                if input1 == "1":
                    print("Returning To Main Menu.")
                    time.sleep(1)
                    print("Returning To Main Menu..")
                    time.sleep(1)
                    print("Returning To Main Menu...")
                    time.sleep(1)
                    main()
                else:
                    print("Invalid Input. Please Try Again.")

        with open("map.csv", "r") as c:
            reader = csv.reader(c)
            array = [row for row in reader]
            for i in range(10):
                for l in range(25):
                    print(array[i][l], end="")
                    if l == 24:
                        print()

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
                time.sleep(1)
                print("Returning to Main Menu..")
                time.sleep(1)
                print("Returning to Main Menu...")
                time.sleep(1)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                main()
            else:
                print("Invalid Input ;(, Please Try Again")

def settings():
    array = [[0] * 25 for _ in range(10)]
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

    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]
    while 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("""
        ██ ██ ███ ███ █ █  █ ███ ██
        █▄ █▄  █   █  █ ██▄█ █ ▄ █▄
        ▄█ █▄  █   █  █ █ ██ █▄█ ▄█""")
        print("Welcome to the settings menu!, Please select an option to continue...")
        print("1 ) Change Charater Name\n2 ) Give Character Gold\n3 ) Give Character Lives\n4 ) Reset Map & Storyline\n5 ) Save Changes\n6 ) Return To Main Menu (Without Saving)")
        input1 = input("> ")
        if input1 == "1":
            print("Please input a new name for your character:")
            charactername = input("> ")
            print("New Character Name:", charactername)
            print("Adding To Bundle Of Changes...")
            time.sleep(3)
        elif input1 == "2":
            print("Please select an option to add gold...\n1 ) +250 Gold\n2 ) +500 Gold\n3 ) +750 Gold\n4 ) +1000 Gold\n5 ) Cancel Action")
            while 1:
                input3 = input("> ")
                if input3 == "1":
                    print("+250 Gold Added To Account")
                    gold = gold + 250
                    print("Adding To Bundle Of Changes...")
                    time.sleep(3)
                    break
                elif input3 == "2":
                    print("+500 Gold Added To Account")
                    gold = gold + 500
                    print("Adding To Bundle Of Changes...")
                    time.sleep(3)
                    break
                elif input3 == "3":
                    print("+750 Gold Added To Account")
                    gold = gold + 750
                    print("Adding To Bundle Of Changes...")
                    time.sleep(3)
                    break
                elif input3 == "4":
                    print("+1000 Gold Added To Account")
                    gold = gold + 1000
                    print("Adding To Bundle Of Changes...")
                    time.sleep(3)
                    break
                elif input3 == "5":
                    print("Returning To Settings.")
                    time.sleep(1)
                    print("Returning To Settings..")
                    time.sleep(1)
                    print("Returning To Settings...")
                    time.sleep(1)
                else:
                    print("Invalid Input, Please Try Again.")
        elif input1 == "3":
            print("Please select an option to add lives...\n1 ) +1 Lives\n2 ) +2 Lives\n3 ) +3 Lives\n4 ) Cancel Action")
            while 1:
                input4 = input("> ")
                if input4 == "1":
                    print("+1 Lives Added To Account")
                    lives = lives + 1
                    print("Adding To Bundle Of Changes...")
                    time.sleep(3)
                    break
                if input4 == "2":
                    print("+2 Lives Added To Account")
                    lives = lives + 2
                    print("Adding To Bundle Of Changes...")
                    time.sleep(3)
                    break
                if input4 == "3":
                    print("+3 Lives Added To Account")
                    lives = lives + 3
                    print("Adding To Bundle Of Changes...")
                    time.sleep(3)
                    break
                elif input4 == "4":
                    print("Returning To Settings.")
                    time.sleep(1)
                    print("Returning To Settings..")
                    time.sleep(1)
                    print("Returning To Settings...")
                    time.sleep(1)
                else:
                    print("Invalid Input, Please Try Again.")
        elif input1 == "4":
            print("Generating New Level")
            for i in range(10):
                for l in range(25):
                    array[i][l] = "#"
            for i in range(10 - 1):
                for l in range(25 - 1):
                    array[i][l] = " "
            for i in range(1):
                for l in range(25):
                    array[i][l] = "#"
            for i in range(10):
                for l in range(1):
                    array[i][l] = "#"
            array[1][1] = "Y"
            while 1:
                a = random.randrange(2, 8)
                b = random.randrange(2, 23)
                if array[a][b] == " ":
                    array[a][b] = "B"
                    break
            while 1:
                a = random.randrange(2, 8)
                b = random.randrange(2, 23)
                if array[a][b] == " ":
                    array[a][b] = "A"
                    break
            while 1:
                a = random.randrange(2, 8)
                b = random.randrange(2, 23)
                if array[a][b] == " ":
                    array[a][b] = "H"
                    break
            time.sleep(1)
            print("Adding To Bundle Of Changes...")
            time.sleep(3)
        elif input1 == "5":
            f.close()
            gold = int(gold)
            lives = int(lives)
            charactername = charactername.strip("\n")
            f = open("data.txt", "w")
            f.write("charactername=")
            f.write(charactername)
            f.write("\n")
            f.write("gold=")
            f.write('%d' % gold)
            f.write("\n")
            f.write("lives=")
            f.write('%d' % lives)
            f.write("\n")
            f.close()
            with open("map.csv", "w", newline="") as c:
                csvWriter = csv.writer(c)
                csvWriter.writerows(array)
            print("Data Saved, Returning to Main Menu.")
            time.sleep(1)
            print("Data Saved, Returning to Main Menu..")
            time.sleep(1)
            print("Data Saved, Returning to Main Menu...")
            time.sleep(1)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            main()
        elif input1 == "6":
            print("Returning to Main Menu.")
            time.sleep(1)
            print("Returning to Main Menu..")
            time.sleep(1)
            print("Returning to Main Menu...")
            time.sleep(1)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            main()
        else:
            print("Invalid Input, Please Try Again...")
            time.sleep(2)
            print("\n\n\n\n\n\n\n\n\n\n\n")

def moveRight():
    array = [[0] * 25 for _ in range(10)]
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
    if array[findingArray[0]][findingArray[1] + 1] == "H":
        print("Entering your house!")
        time.sleep(1)
        house()
    if array[findingArray[0]][findingArray[1] + 1] == "A":
        print("Opening Convosation With Adam!")
        time.sleep(1)
        adam()
    if array[findingArray[0]][findingArray[1] + 1] == "F":
        print("Opening Convosation With Frank!")
        time.sleep(1)
        frank()
    if array[findingArray[0]][findingArray[1] + 1] == "J":
        print("Opening Convosation With Jay!")
        time.sleep(1)
        jay()
    if array[findingArray[0]][findingArray[1] + 1] == "Z":
        print("Opening Convosation With Zane!")
        time.sleep(1)
        zane()
    if array[findingArray[0]][findingArray[1] + 1] == "G":
        print("Opening Convosation With Greg!")
        time.sleep(1)
        greg()
    if array[findingArray[0]][findingArray[1] + 1] == "S":
        print("Opening Convosation With Sam!")
        time.sleep(1)
        sam()
    if array[findingArray[0]][findingArray[1] + 1] == "T":
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
        print("You have cut down a tree and collected its wood.")
        time.sleep(1)
        print("You have cut down a tree and collected its wood..")
        time.sleep(1)
        print("You have cut down a tree and collected its wood...")
        time.sleep(1)
        print("+ 50 Gold")
        time.sleep(3)
        gold = gold + 50
        f.close()
        gold = int(gold)
        charactername = charactername.strip("\n")
        f = open("data.txt", "w")
        f.write("charactername=")
        f.write(charactername)
        f.write("\n")
        f.write("gold=")
        f.write('%d' % gold)
        f.write("\n")
        f.write("lives=")
        f.write('%d' % lives)
        f.write("\n")
        f.close()
        array[findingArray[0]][findingArray[1] + 1] = " "

    array[findingArray[0]][findingArray[1]] = " "
    array[findingArray[0]][findingArray[1] + 1] = "Y"

    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    play()

def moveLeft():
    array = [[0] * 25 for _ in range(10)]
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
    if array[findingArray[0]][findingArray[1] - 1] == "H":
        print("Entering your house!")
        time.sleep(1)
        house()
    if array[findingArray[0]][findingArray[1] - 1] == "A":
        print("Opening Convosation With Adam!")
        time.sleep(1)
        adam()
    if array[findingArray[0]][findingArray[1] - 1] == "F":
        print("Opening Convosation With Frank!")
        time.sleep(1)
        frank()
    if array[findingArray[0]][findingArray[1] - 1] == "J":
        print("Opening Convosation With Jay!")
        time.sleep(1)
        jay()
    if array[findingArray[0]][findingArray[1] - 1] == "Z":
        print("Opening Convosation With Zane!")
        time.sleep(1)
        zane()
    if array[findingArray[0]][findingArray[1] - 1] == "G":
        print("Opening Convosation With Greg!")
        time.sleep(1)
        greg()
    if array[findingArray[0]][findingArray[1] - 1] == "S":
        print("Opening Convosation With Sam!")
        time.sleep(1)
        sam()
    if array[findingArray[0]][findingArray[1] - 1] == "T":
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
        print("You have cut down a tree and collected its wood.")
        time.sleep(1)
        print("You have cut down a tree and collected its wood..")
        time.sleep(1)
        print("You have cut down a tree and collected its wood...")
        time.sleep(1)
        print("+ 50 Gold")
        time.sleep(3)
        gold = gold + 50
        f.close()
        gold = int(gold)
        charactername = charactername.strip("\n")
        f = open("data.txt", "w")
        f.write("charactername=")
        f.write(charactername)
        f.write("\n")
        f.write("gold=")
        f.write('%d' % gold)
        f.write("\n")
        f.write("lives=")
        f.write('%d' % lives)
        f.write("\n")
        f.close()
        array[findingArray[0]][findingArray[1] + 1] = " "

    array[findingArray[0]][findingArray[1]] = " "
    array[findingArray[0]][findingArray[1] - 1] = "Y"

    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    play()

def moveUp():
    array = [[0] * 25 for _ in range(10)]
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
    if array[findingArray[0] - 1][findingArray[1]] == "H":
        print("Entering your house!")
        time.sleep(1)
        house()
    if array[findingArray[0] - 1][findingArray[1]] == "A":
        print("Opening Convosation With Adam!")
        time.sleep(1)
        adam()
    if array[findingArray[0] - 1][findingArray[1]] == "F":
        print("Opening Convosation With Frank!")
        time.sleep(1)
        frank()
    if array[findingArray[0] - 1][findingArray[1]] == "J":
        print("Opening Convosation With Jay!")
        time.sleep(1)
        jay()
    if array[findingArray[0] - 1][findingArray[1]] == "Z":
        print("Opening Convosation With Zane!")
        time.sleep(1)
        zane()
    if array[findingArray[0] - 1][findingArray[1]] == "G":
        print("Opening Convosation With Greg!")
        time.sleep(1)
        greg()
    if array[findingArray[0] - 1][findingArray[1]] == "S":
        print("Opening Convosation With Sam!")
        time.sleep(1)
        sam()
    if array[findingArray[0] - 1][findingArray[1]] == "T":
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
        print("You have cut down a tree and collected its wood.")
        time.sleep(1)
        print("You have cut down a tree and collected its wood..")
        time.sleep(1)
        print("You have cut down a tree and collected its wood...")
        time.sleep(1)
        print("+ 50 Gold")
        time.sleep(3)
        gold = gold + 50
        f.close()
        gold = int(gold)
        charactername = charactername.strip("\n")
        f = open("data.txt", "w")
        f.write("charactername=")
        f.write(charactername)
        f.write("\n")
        f.write("gold=")
        f.write('%d' % gold)
        f.write("\n")
        f.write("lives=")
        f.write('%d' % lives)
        f.write("\n")
        f.close()
        array[findingArray[0]][findingArray[1] + 1] = " "

    array[findingArray[0]][findingArray[1]] = " "
    array[findingArray[0] - 1][findingArray[1]] = "Y"

    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    play()

def moveDown():
    array = [[0] * 25 for _ in range(10)]
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
    if array[findingArray[0] + 1][findingArray[1]] == "H":
        print("Entering your house!")
        time.sleep(1)
        house()
    if array[findingArray[0] + 1][findingArray[1]] == "A":
        print("Opening Convosation With Adam!")
        time.sleep(1)
        adam()
    if array[findingArray[0] + 1][findingArray[1]] == "F":
        print("Opening Convosation With Frank!")
        time.sleep(1)
        frank()
    if array[findingArray[0] + 1][findingArray[1]] == "J":
        print("Opening Convosation With Jay!")
        time.sleep(1)
        jay()
    if array[findingArray[0] + 1][findingArray[1]] == "Z":
        print("Opening Convosation With Zane!")
        time.sleep(1)
        zane()
    if array[findingArray[0] + 1][findingArray[1]] == "G":
        print("Opening Convosation With Greg!")
        time.sleep(1)
        greg()
    if array[findingArray[0] + 1][findingArray[1]] == "S":
        print("Opening Convosation With Sam!")
        time.sleep(1)
        sam()
    if array[findingArray[0] + 1][findingArray[1]] == "T":
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
        print("You have cut down a tree and collected its wood.")
        time.sleep(1)
        print("You have cut down a tree and collected its wood..")
        time.sleep(1)
        print("You have cut down a tree and collected its wood...")
        time.sleep(1)
        print("+ 50 Gold")
        time.sleep(3)
        gold = gold + 50
        f.close()
        gold = int(gold)
        charactername = charactername.strip("\n")
        f = open("data.txt", "w")
        f.write("charactername=")
        f.write(charactername)
        f.write("\n")
        f.write("gold=")
        f.write('%d' % gold)
        f.write("\n")
        f.write("lives=")
        f.write('%d' % lives)
        f.write("\n")
        f.close()
        array[findingArray[0]][findingArray[1] + 1] = " "

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
        print("\nWelcome to the bar,", charactername, "Please select an option:\n1 - Gamble, 2 - Exit, 5 - Talk to Bartender In Private | Gold:", gold)
        input1 = input("> ")
        if input1 == "1":
            print("Please enter the amount you would like to gamble, Must be above 50 or below 250")
            while 1:
                input2 = int(input("> "))
                if input2 <= gold:
                    if input2 <= 250:
                        if input2 >= 50:
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
            gold = gold - input2
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
                    gold = gold + input2 * 2
                else:
                    print("Sorry, you have lost the money that you have bet.")
            elif result < 50:
                print("The Result Was: Tails!")
                if coin == "false":
                    print("Congratulations, you have doubled your money!")
                    print("+ ", input2 * 2, "gold.")
                    gold = gold + input2 * 2
                else:
                    print("Sorry, you have lost the money that you have bet.")
            else:
                print("It was a draw!, Your money was refunded.")
                print("+ ", input2, " gold.")
                gold = gold + input2
        elif input1 == "2":
            f.close()
            gold = int(gold)
            charactername = charactername.strip("\n")
            f = open("data.txt", "w")
            f.write("charactername=")
            f.write(charactername)
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
        elif input1 == "5":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhats the password?")
            input4 = input("> ")
            if input4 == "Adam44":
                array = [[0] * 25 for _ in range(10)]
                with open("map.csv", "r") as c:
                    reader = csv.reader(c)
                    array = [row for row in reader]
                for i in range(len(array)):
                    for l in range(len(array[i])):
                        if array[i][l] == "Z":
                            print("\n\n\nZack - You have already been here. Go away.")
                            time.sleep(3)
                            play()
                        if array[i][l] == "J":
                            print("\n\n\nZack - You have already been here. Go away.")
                            time.sleep(3)
                            play()
                        if array[i][l] == "F":
                            print("\n\n\nZack - You have already been here. Go away.")
                            time.sleep(3)
                            play()
                        if array[i][l] == "A":
                            print("\n\n\nZack - You cheating lol, go talk to Adam.")
                            time.sleep(3)
                            play()
                        if array[i][l] == "G":
                            print("\n\n\nZack - You are not able to return here.")
                            time.sleep(3)
                            play()
                        if array[i][l] == "S":
                            print("\n\n\nZack - You are not able to return here.")
                            time.sleep(3)
                            play()
                print("Zack - So your the new guy everyones talking about, Huh...")
                time.sleep(2)
                print("Zack - We've been having some issues with some thugs around here, you look well, capable...")
                time.sleep(2)
                print("Zack - Here's a deal for you, get them out of town and I will give you 250 Gold & Protection...")
                time.sleep(2)
                print("\n1 ) Who are the thugs?\n2 ) Protection from what?\n3 ) Accept Mission")
                while 1:
                    input5 = input("> ")
                    if input5 == "1":
                        print(charactername.strip("\n"), "- Who are the thugs?")
                        time.sleep(2)
                        print("Zack - Frank, Jay and Zane. You won't miss them, you can see them from a mile away.")
                    elif input5 == "2":
                        print(charactername.strip("\n"), "- Protection from what?")
                        time.sleep(2)
                        print("Zack - Thats none of your concern, as of right now.")
                    elif input5 == "3":
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print(charactername.strip("\n"), "- Okay... I will do it...")
                        time.sleep(2)
                        print("Zack - You made the right choice...")
                        time.sleep(1)
                        print("\nYou leave the bar.")
                        time.sleep(1)
                        while 1:
                            a = random.randrange(1, 9)
                            b = random.randrange(1, 24)
                            if array[a][b] == " ":
                                array[a][b] = "F"
                                break
                        while 1:
                            a = random.randrange(1, 9)
                            b = random.randrange(1, 24)
                            if array[a][b] == " ":
                                array[a][b] = "J"
                                break
                        while 1:
                            a = random.randrange(1, 9)
                            b = random.randrange(1, 24)
                            if array[a][b] == " ":
                                array[a][b] = "Z"
                                break
                        print("\nYou leave the bar..")
                        time.sleep(1)
                        print("\nYou leave the bar...")
                        time.sleep(1)
                        with open("map.csv", "w", newline="") as c:
                            csvWriter = csv.writer(c, delimiter=',')
                            csvWriter.writerows(array)
                        play()
            else:
                print("Thats not the password... Get out of my bar now...")
                time.sleep(2)
                print("You get kicked out the bar...")
                time.sleep(2)
                f.close()
                gold = int(gold)
                charactername = charactername.strip("\n")
                f = open("data.txt", "w")
                f.write("charactername=")
                f.write(charactername)
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

def adam():
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
███████████████████████████
██▀▄─██▄─▄▄▀██▀▄─██▄─▀█▀─▄█
██─▀─███─██─██─▀─███─█▄█─██
▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀""")

    print("Adam - Hello traveller, whats your name?\n1 ) Tell Real Name\n2 ) Tell Fake Name")
    input1 = input("> ")
    if input1 == "1":
        print(charactername.strip("\n"), "- My name is", charactername.strip("\n"), ", Nice to meet you.")
        time.sleep(1)
        print("Adam - Well it was nice to meet you,", charactername.strip("\n"), "I'm currently leaving town to get another job,")
        print("to get started contact the bartender with option 5 and tell him the password: Adam44.")
    elif input1 == "2":
        print(charactername.strip("\n"), "- My name is Mickenzie.")
        time.sleep(1)
        print("Adam - Well it was nice to meet you, Mickenzie. I'm currently leaving town to get another job,")
        print("to get started contact the bartender with option 5 and tell him the password: Adam44.")
    else:
        print(charactername.strip("\n"), "- ...")
        time.sleep(1)
        print("Adam - Well it was nice to meet you, No need to be rude but I'm currently leaving town to get another job,")
        print("to get started contact the bartender with option 5 and tell him the password: Adam44.")
    time.sleep(7)
    print("1 ) Acknowledge and Leave")
    while 1:
        input2 = input("> ")
        if input2 == "1":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            time.sleep(1)
            print("Adam - Good Luck...")
            print("Adam walks out of town into the fog...")
            time.sleep(3)
            f.close()
            gold = int(gold)
            charactername = charactername.strip("\n")
            f = open("data.txt", "w")
            f.write("charactername=")
            f.write(charactername)
            f.write("\n")
            f.write("gold=")
            f.write('%d' % gold)
            f.write("\n")
            f.write("lives=")
            f.write('%d' % lives)
            f.write("\n")
            f.close()
            # Removing adam from the map
            array = [[0] * 25 for _ in range(10)]
            findingArray = []
            with open("map.csv", "r") as c:
                reader = csv.reader(c)
                array = [row for row in reader]

            for i in range(len(array)):
                for l in range(len(array[i])):
                    if array[i][l] == "A":
                        findingArray.append(i)
                        findingArray.append(l)

            array[findingArray[0]][findingArray[1]] = " "

            with open("map.csv", "w", newline="") as c:
                csvWriter = csv.writer(c, delimiter=',')
                csvWriter.writerows(array)
            print("Data Saved, Returning To Main Game")
            play()

def frank():
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
██████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░█
█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░███
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀░░█
█░░░░░░█████████░░░░░░██░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████████████""")

    print("Frank - Hey, Whats up?\n1 ) Ask To Leave Nicely\n2 ) Try To Bribe\n3 ) Fight")
    while 1:
        input1 = input("> ")
        if input1 == "1":
            print(charactername.strip("\n"), "- You Need To Leave...")
            time.sleep(1)
            print("Frank - Whys that?")
            time.sleep(1)
            print(charactername.strip("\n"), "- The Bartender Says So, Your not welcome here any longer.")
            time.sleep(1)
            print("Frank - Well, Thats not going to happen, Me, Zane & Jay arent going nowhere.")
            time.sleep(1)
            print("\n2 ) Try To Bribe\n3 ) Fight")
        elif input1 == "2":
            print(charactername.strip("\n"), "Say I gave you some gold, would you mind leaving?")
            time.sleep(1)
            print("Frank - Depends how much... How much you offering...")
            time.sleep(1)
            print("\n1 ) 100 Gold\n2 ) 250 Gold\n3 ) All Gold")
            while 1:
                input2 = input("> ")
                if input2 == "1":
                    print("Frank - Not enough mate, Thats not gonna get my anywhere...")
                    time.sleep(1)
                    print("Frank - Get out of here before I knock your out mate...")
                    time.sleep(1)
                    print("\n3 ) Fight")
                    break
                elif input2 == "2":
                    print("Frank - Ehh, Reasonable but im sure you have more...")
                    time.sleep(1)
                    print("Frank - How about I beat you up and we will see for sure tough guy!")
                    time.sleep(1)
                    print("\n3 ) Fight")
                    break
                elif input2 == "3":
                    if gold > 500:
                        print("Frank - Fine, That will probably be enough. Goodbye...")
                        time.sleep(3)
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        time.sleep(2)
                        print("Frank Leaves Town...")
                        gold = 0
                        time.sleep(3)
                        f.close()
                        gold = int(gold)
                        charactername = charactername.strip("\n")
                        f = open("data.txt", "w")
                        f.write("charactername=")
                        f.write(charactername)
                        f.write("\n")
                        f.write("gold=")
                        f.write('%d' % gold)
                        f.write("\n")
                        f.write("lives=")
                        f.write('%d' % lives)
                        f.write("\n")
                        f.close()
                        # Removing frank from the map
                        array = [[0] * 25 for _ in range(10)]
                        findingArray = []
                        with open("map.csv", "r") as c:
                            reader = csv.reader(c)
                            array = [row for row in reader]

                        for i in range(len(array)):
                            for l in range(len(array[i])):
                                if array[i][l] == "F":
                                    findingArray.append(i)
                                    findingArray.append(l)

                        array[findingArray[0]][findingArray[1]] = " "

                        with open("map.csv", "w", newline="") as c:
                            csvWriter = csv.writer(c, delimiter=',')
                            csvWriter.writerows(array)
                        print("Data Saved, Returning To Main Game")
                        play()
                    else:
                        print("Still not enough buddy...")
                        print("\n3 ) Fight")
                        break
        elif input1 == "3":
            enemyattack = 3
            enemydefence = 4
            attack = 5
            defence = 5
            time.sleep(1)
            print("Begining Fight With Frank...")
            time.sleep(1)
            while 1:
                if defence <= 0:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("You have lost the battle ;(")
                    print("-1 Lives")
                    lives - 1
                    time.sleep(2)
                    print("Frank Decides To Leave Town & Get Medical Care...")
                    time.sleep(5)
                    f.close()
                    gold = int(gold)
                    charactername = charactername.strip("\n")
                    f = open("data.txt", "w")
                    f.write("charactername=")
                    f.write(charactername)
                    f.write("\n")
                    f.write("gold=")
                    f.write('%d' % gold)
                    f.write("\n")
                    f.write("lives=")
                    f.write('%d' % lives)
                    f.write("\n")
                    f.close()
                    # Removing frank from the map
                    array = [[0] * 25 for _ in range(10)]
                    findingArray = []
                    with open("map.csv", "r") as c:
                        reader = csv.reader(c)
                        array = [row for row in reader]

                    for i in range(len(array)):
                        for l in range(len(array[i])):
                            if array[i][l] == "F":
                                findingArray.append(i)
                                findingArray.append(l)

                    array[findingArray[0]][findingArray[1]] = " "

                    with open("map.csv", "w", newline="") as c:
                        csvWriter = csv.writer(c, delimiter=',')
                        csvWriter.writerows(array)
                    print("Data Saved, Returning To Main Game")
                    play()
                if enemydefence <= 0:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("You have won the battle!")
                    time.sleep(2)
                    print("Frank Leaves Town Having Sustained Bad Injuries...")
                    time.sleep(5)
                    f.close()
                    gold = int(gold)
                    charactername = charactername.strip("\n")
                    f = open("data.txt", "w")
                    f.write("charactername=")
                    f.write(charactername)
                    f.write("\n")
                    f.write("gold=")
                    f.write('%d' % gold)
                    f.write("\n")
                    f.write("lives=")
                    f.write('%d' % lives)
                    f.write("\n")
                    f.close()
                    # Removing frank from the map
                    array = [[0] * 25 for _ in range(10)]
                    findingArray = []
                    with open("map.csv", "r") as c:
                        reader = csv.reader(c)
                        array = [row for row in reader]

                    for i in range(len(array)):
                        for l in range(len(array[i])):
                            if array[i][l] == "F":
                                findingArray.append(i)
                                findingArray.append(l)

                    array[findingArray[0]][findingArray[1]] = " "

                    with open("map.csv", "w", newline="") as c:
                        csvWriter = csv.writer(c, delimiter=',')
                        csvWriter.writerows(array)
                    print("Data Saved, Returning To Main Game")
                    play()
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("""
(._.)
<|>
_/\_""")
                while 1:
                    frankAttack = random.randrange(1, 6)
                    if frankAttack == 1:
                        if enemyattack < 3:
                             continue
                        defence = defence - 2
                        enemyattack = enemyattack - 3
                        print("Frank - feels weakened, Loses 2 Attack Power")
                        time.sleep(1)
                        print(charactername.strip("\n"), "- Takes a punch to the face, Loses 2 Defence.")
                        time.sleep(3)
                        break
                    elif frankAttack == 2:
                        if enemyattack < 1:
                             continue
                        defence = defence - 1
                        enemyattack = enemyattack - 1
                        print("Frank - feels weakened, Loses 1 Attack Power")
                        time.sleep(1)
                        print(charactername.strip("\n"), "Gets kicked, Loses 1 Defence.")
                        time.sleep(3)
                        break
                    elif frankAttack == 3:
                        if enemyattack < 2:
                             continue
                        defence = defence - 2
                        enemyattack = enemyattack - 2
                        print("Frank - feels weakened, Loses 2 Attack Power")
                        time.sleep(1)
                        print(charactername.strip("\n"), "- Gets barged, Loses 2 Defence.")
                        time.sleep(3)
                        break
                    elif frankAttack == 4:
                        enemyattack = enemyattack + 1
                        enemydefence = enemydefence + 1
                        print("Frank - Takes cover, and gains strength. Gains 1 Attack Power & 1 Defence")
                        time.sleep(3)
                        break
                    elif frankAttack == 5:
                        enemyattack = enemyattack + 2
                        enemydefence = enemydefence + 1
                        print("Frank - Stops fighting temporarily, Gains 2 Attack Power & 1 Defence")
                        time.sleep(3)
                        break
                    elif frankAttack == 6:
                        enemyattack = enemyattack + 3
                        print("Frank - Recharges Abilities, Gains 3 Attack Power")
                        time.sleep(3)
                        break
                    else:
                        print("Frank fails his current action.")
                print("\nEnter A Character To Interact: A - Attack, D - Defend")
                print("Attack:", attack, "| Defence:", defence, "| Lives:", lives)
                print("Enemy Attack:", enemyattack, "| Enemy Defence:", enemydefence, "\n")
                while 1:
                    input3 = input("> ").upper()
                    if input3 == "A":
                        print("\nAttack Moves:\n1 ) Punch [Frank: -2 Defence, You: -3 Attack]\n2 ) Kick [Frank: -1 Defence, You: -1 Attack]\n3 ) Barge [Frank: -2 Defence, You: -2 Attack]")
                        while 1:
                            input4 = input("> ")
                            if input4 == "1":
                                if attack < 3:
                                    print("Not enough Attack Power, Cancelling Move.")
                                    time.sleep(4)
                                    break
                                enemydefence = enemydefence - 2
                                attack = attack - 3
                                print("Frank - Takes a punch to the face, Loses 2 Defence.")
                                time.sleep(1)
                                print(charactername.strip("\n"), "- feels weakened, Loses 2 Attack Power")
                                time.sleep(3)
                                break
                            elif input4 == "2":
                                if attack < 1:
                                    print("Not enough Attack Power, Cancelling Move.")
                                    time.sleep(4)
                                    break
                                enemydefence = enemydefence - 1
                                attack = attack - 1
                                print("Frank - Gets kicked, Loses 1 Defence.")
                                time.sleep(1)
                                print(charactername.strip("\n"), "- feels weakened, Loses 1 Attack Power")
                                time.sleep(3)
                                break
                            elif input4 == "3":
                                if attack < 2:
                                    print("Not enough Attack Power, Cancelling Move.")
                                    time.sleep(4)
                                    break
                                enemydefence = enemydefence - 2
                                attack = attack - 2
                                print("Frank - Gets barged, Loses 2 Defence.")
                                time.sleep(1)
                                print(charactername.strip("\n"), "- feels weakened, Loses 2 Attack Power")
                                time.sleep(3)
                                break
                            else:
                                print("Invalid Input, Please enter 1, 2 or 3...")
                    elif input3 == "D":
                        print("\nDefence Moves:\n1 ) Take Cover [You: +2 Defence +1 Attack]\n2 ) Dodge [You: +1 Defence +2 Attack]\n3 ) Recharge [You: +3 Attack]")
                        while 1:
                            input4 = input("> ")
                            if input4 == "1":
                                attack = attack + 1
                                defence = defence + 2
                                print(charactername.strip("\n"), "- Takes cover, you gain your strength. Gains 1 Attack Power & 2 Defence")
                                time.sleep(3)
                                break
                            elif input4 == "2":
                                attack = attack + 2
                                defence = defence + 1
                                print(charactername.strip("\n"), "- Stops fighting temporarily, Gains 2 Attack Power & 1 Defence")
                                time.sleep(3)
                                break
                            elif input4 == "3":
                                attack = attack + 3
                                print(charactername.strip("\n"), "- Recharges Abilities, Gains 3 Attack Power")
                                time.sleep(3)
                                break
                            else:
                                print("Invalid Input, Please enter 1, 2 or 3...")
                    else:
                        print("Invalid Input, Please enter A or D...")
                    break
        else:
            print("Invalid Input, Please enter 1, 2 or 3...")

def jay():
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
██████████████████████████████████████████████████
█████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█
█████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█
█████████░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█
█████████░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░███
█████████░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░░░▄▀▄▀▄▀░░░░███
█████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████
█░░░░░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███████░░▄▀░░███████
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████
█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░███████░░░░░░███████
██████████████████████████████████████████████████""")

    print("Jay - What do you want kid?\n1 ) Threaten To Leave\n2 ) Attempt Robbery\n3 ) Fight")
    while 1:
        input1 = input("> ")
        if input1 == "1":
            print(charactername.strip("\n"), "- Your not welcome here Jay, Leave or I will make you...")
            time.sleep(2)
            print("Jay - Oh really... A wrap scallion from out of towns going to make me leave huh!")
            time.sleep(2)
            print(charactername.strip("\n"), "- If you dont leave you will leave me no choice.")
            time.sleep(2)
            print("Jay pushes you over and takes half of your gold.")
            stolenAmount = gold // 2
            gold - stolenAmount
            time.sleep(1)
            print("\n2 ) Attempt Revenge Robbery\n3 ) Fight")
        elif input1 == "2":
            print(charactername.strip("\n"), "- Hey look over there...")
            time.sleep(1)
            print("Jay turns around to look what you are pointing at.")
            time.sleep(2)
            print("You manage to steal 98 Gold.")
            gold = gold + 98
            time.sleep(2)
            print("Jay - HEY, WHAT WAS THAT FOR!")
            print("\n3 ) Fight")
        elif input1 == "3":
            enemyattack = 5
            enemydefence = 5
            attack = 5
            defence = 6
            time.sleep(1)
            print("Begining Fight With Jay...")
            time.sleep(1)
            while 1:
                if defence <= 0:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("You have lost the battle ;(")
                    print("-1 Lives")
                    lives - 1
                    time.sleep(2)
                    print("Jay Leaves Town To Get Medical Care With An Angry Look On His Face...")
                    time.sleep(5)
                    f.close()
                    gold = int(gold)
                    charactername = charactername.strip("\n")
                    f = open("data.txt", "w")
                    f.write("charactername=")
                    f.write(charactername)
                    f.write("\n")
                    f.write("gold=")
                    f.write('%d' % gold)
                    f.write("\n")
                    f.write("lives=")
                    f.write('%d' % lives)
                    f.write("\n")
                    f.close()
                    # Removing jay from the map
                    array = [[0] * 25 for _ in range(10)]
                    findingArray = []
                    with open("map.csv", "r") as c:
                        reader = csv.reader(c)
                        array = [row for row in reader]

                    for i in range(len(array)):
                        for l in range(len(array[i])):
                            if array[i][l] == "J":
                                findingArray.append(i)
                                findingArray.append(l)

                    array[findingArray[0]][findingArray[1]] = " "

                    with open("map.csv", "w", newline="") as c:
                        csvWriter = csv.writer(c, delimiter=',')
                        csvWriter.writerows(array)
                    print("Data Saved, Returning To Main Game")
                    play()
                if enemydefence <= 0:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("You have won the battle!")
                    time.sleep(2)
                    print("Jay Leaves Town In An Ambulance...")
                    time.sleep(5)
                    f.close()
                    gold = int(gold)
                    charactername = charactername.strip("\n")
                    f = open("data.txt", "w")
                    f.write("charactername=")
                    f.write(charactername)
                    f.write("\n")
                    f.write("gold=")
                    f.write('%d' % gold)
                    f.write("\n")
                    f.write("lives=")
                    f.write('%d' % lives)
                    f.write("\n")
                    f.close()
                    # Removing jay from the map
                    array = [[0] * 25 for _ in range(10)]
                    findingArray = []
                    with open("map.csv", "r") as c:
                        reader = csv.reader(c)
                        array = [row for row in reader]

                    for i in range(len(array)):
                        for l in range(len(array[i])):
                            if array[i][l] == "J":
                                findingArray.append(i)
                                findingArray.append(l)

                    array[findingArray[0]][findingArray[1]] = " "

                    with open("map.csv", "w", newline="") as c:
                        csvWriter = csv.writer(c, delimiter=',')
                        csvWriter.writerows(array)
                    print("Data Saved, Returning To Main Game")
                    play()
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("""
            (`-`)
            -|-
            _/\_""")
                while 1:
                    jayAttack = random.randrange(1, 6)
                    if jayAttack == 1:
                        if enemyattack < 3:
                            continue
                        defence = defence - 2
                        enemyattack = enemyattack - 3
                        print("Jay - feels weakened, Loses 2 Attack Power")
                        time.sleep(1)
                        print(charactername.strip("\n"), "- Takes a punch to the face, Loses 2 Defence.")
                        time.sleep(3)
                        break
                    elif jayAttack == 2:
                        if enemyattack < 1:
                            continue
                        defence = defence - 1
                        enemyattack = enemyattack - 1
                        print("Jay - feels weakened, Loses 1 Attack Power")
                        time.sleep(1)
                        print(charactername.strip("\n"), "Gets kicked, Loses 1 Defence.")
                        time.sleep(3)
                        break
                    elif jayAttack == 3:
                        if enemyattack < 2:
                            continue
                        defence = defence - 2
                        enemyattack = enemyattack - 2
                        print("Jay - feels weakened, Loses 2 Attack Power")
                        time.sleep(1)
                        print(charactername.strip("\n"), "- Gets barged, Loses 2 Defence.")
                        time.sleep(3)
                        break
                    elif jayAttack == 4:
                        enemyattack = enemyattack + 1
                        enemydefence = enemydefence + 1
                        print("Jay - Takes cover, and gains strength. Gains 1 Attack Power & 1 Defence")
                        time.sleep(3)
                        break
                    elif jayAttack == 5:
                        enemyattack = enemyattack + 2
                        enemydefence = enemydefence + 1
                        print("Jay - Stops fighting temporarily, Gains 2 Attack Power & 1 Defence")
                        time.sleep(3)
                        break
                    elif jayAttack == 6:
                        enemyattack = enemyattack + 3
                        print("Jay - Recharges Abilities, Gains 3 Attack Power")
                        time.sleep(3)
                        break
                    else:
                        print("Jay fails his current action.")
                print("\nEnter A Character To Interact: A - Attack, D - Defend")
                print("Attack:", attack, "| Defence:", defence, "| Lives:", lives)
                print("Enemy Attack:", enemyattack, "| Enemy Defence:", enemydefence, "\n")
                while 1:
                    input3 = input("> ").upper()
                    if input3 == "A":
                        print(
                            "\nAttack Moves:\n1 ) Punch [Jay: -2 Defence, You: -3 Attack]\n2 ) Kick [Jay: -1 Defence, You: -1 Attack]\n3 ) Barge [Jay: -2 Defence, You: -2 Attack]")
                        while 1:
                            input4 = input("> ")
                            if input4 == "1":
                                if attack < 3:
                                    print("Not enough Attack Power, Cancelling Move.")
                                    time.sleep(4)
                                    break
                                enemydefence = enemydefence - 2
                                attack = attack - 3
                                print("Jay - Takes a punch to the face, Loses 2 Defence.")
                                time.sleep(1)
                                print(charactername.strip("\n"), "- feels weakened, Loses 2 Attack Power")
                                time.sleep(3)
                                break
                            elif input4 == "2":
                                if attack < 1:
                                    print("Not enough Attack Power, Cancelling Move.")
                                    time.sleep(4)
                                    break
                                enemydefence = enemydefence - 1
                                attack = attack - 1
                                print("Jay - Gets kicked, Loses 1 Defence.")
                                time.sleep(1)
                                print(charactername.strip("\n"), "- feels weakened, Loses 1 Attack Power")
                                time.sleep(3)
                                break
                            elif input4 == "3":
                                if attack < 2:
                                    print("Not enough Attack Power, Cancelling Move.")
                                    time.sleep(4)
                                    break
                                enemydefence = enemydefence - 2
                                attack = attack - 2
                                print("Jay - Gets barged, Loses 2 Defence.")
                                time.sleep(1)
                                print(charactername.strip("\n"), "- feels weakened, Loses 2 Attack Power")
                                time.sleep(3)
                                break
                            else:
                                print("Invalid Input, Please enter 1, 2 or 3...")
                    elif input3 == "D":
                        print(
                            "\nDefence Moves:\n1 ) Take Cover [You: +2 Defence +1 Attack]\n2 ) Dodge [You: +1 Defence +2 Attack]\n3 ) Recharge [You: +3 Attack]")
                        while 1:
                            input4 = input("> ")
                            if input4 == "1":
                                attack = attack + 1
                                defence = defence + 2
                                print(charactername.strip("\n"),
                                      "- Takes cover, you gain your strength. Gains 1 Attack Power & 2 Defence")
                                time.sleep(3)
                                break
                            elif input4 == "2":
                                attack = attack + 2
                                defence = defence + 1
                                print(charactername.strip("\n"),
                                      "- Stops fighting temporarily, Gains 2 Attack Power & 1 Defence")
                                time.sleep(3)
                                break
                            elif input4 == "3":
                                attack = attack + 3
                                print(charactername.strip("\n"), "- Recharges Abilities, Gains 3 Attack Power")
                                time.sleep(3)
                                break
                            else:
                                print("Invalid Input, Please enter 1, 2 or 3...")
                    else:
                        print("Invalid Input, Please enter A or D...")
                    break
        else:
            print("Invalid Input, Please enter 1, 2 or 3...")

def zane():
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
█████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█████████░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░█████████
███████░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
███░░░░▄▀░░░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░░░▄▀░░░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████
█░░▄▀▄▀░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█
█████████████████████████████████████████████████████████████████████████""")

    array = [[0] * 25 for _ in range(10)]
    findingArray = []
    findingArray2 = []
    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]
    print("Zane - I saw what you did?\n1 ) What did I do?")
    while 1:
        input1 = input("> ")
        if input1 == "1":
            print(charactername.strip("\n"), "- What did I do?")
            time.sleep(2)
            print("Zane - I saw you talking to the bartender, I know your a threat to our gang...")
            time.sleep(2)
            print("\n1 ) Calm Down\n2 ) Didnt Ask")
            while 1:
                input2 = input("> ")
                if input2 == "1":
                    print(charactername.strip("\n"), "- You need to calm down...")
                    time.sleep(2)
                    print("Zane - I WILL NOT CALM DOWN, YOU ARE HERE TO TRY AND MAKE ME LEAVE")
                    time.sleep(2)
                    print("\n1 ) I Will Make You Leave\n2 ) Im not sure what your talking about...")
                    while 1:
                        input3 = input("> ")
                        if input3 == "1":
                            print(charactername.strip("\n"), "- Thats exactly what Im planning to do...")
                            time.sleep(2)
                            print("Zane - THAT WILL NEVER HAPPEN")
                            time.sleep(2)
                            print("Zane - THIS IS MY TOWN!!!")
                            break
                        elif input3 == "2":
                            print(charactername.strip("\n"), "- Im not sure what your talking about...")
                            time.sleep(2)
                            print("Zane - LIAR!")
                            time.sleep(2)
                            print("\n1 ) Im not lying!\n2 ) Fine, I was lying. You need to leave...")
                            while 1:
                                input4 = input("> ")
                                if input4 == "1":
                                    print(charactername.strip("\n"), "- Im not lying!")
                                    time.sleep(2)
                                    print("Zane - LIAR! THATS IT!")
                                    break
                                elif input4 == "2":
                                    print(charactername.strip("\n"), "- Fine, I was Lying. You need to leave...")
                                    time.sleep(2)
                                    print("Zane - Finally You admit it. You Wrap Scallion.")
                                    break
                                else:
                                    print("Invalid Input, Please enter 1 or 2")
                            break
                        else:
                            print("Invalid Input, Please enter 1 or 2...")
                    break
                elif input2 == "2":
                    print(charactername.strip("\n"), "- Didnt Ask")
                    time.sleep(2)
                    print("Zane - EXCUSE ME!")
                    time.sleep(2)
                    print(charactername.strip("\n"), "- You Heard Me...")
                    time.sleep(2)
                    print("Zane - I see how it is, Last Time someone said that I blew up their house...")
                    time.sleep(2)
                    print("\n1 ) Really?\n2 ) Didnt ask")
                    while 1:
                        input5 = input("> ")
                        if input5 == "1":
                            print(charactername.strip("\n"), "- Really?")
                            time.sleep(2)
                            print("Zane - I dont say things twice!, I blew up his home and made sure he never returned...")
                            time.sleep(2)
                            print("\n1 ) Can you repeat that please...\n2 ) Okay Then...")
                            while 1:
                                input6 = input("> ")
                                if input6 == "1":
                                    print(charactername.strip("\n"), "- Can you repeat that please?")
                                    time.sleep(2)
                                    print("Zane - NO")
                                    break
                                elif input6 == "2":
                                    print(charactername.strip("\n"), "- Okay then...")
                                    time.sleep(2)
                                    print("Zane - ...")
                                    break
                                else:
                                    print("Invalid Input, Please enter 1 or 2...")
                                break
                            break
                        elif input5 == "2":
                            print(charactername.strip("\n"), "- Didnt Ask")
                            time.sleep(2)
                            print("Zane - THATS IT!")
                            break
                        else:
                            print("Invalid Input, Please enter 1 or 2...")
                    break
                else:
                    print("Invalid Input, Please Enter 1, 2 or 3...")
            time.sleep(3)
            print("Zane - Guess what :)")
            time.sleep(2)
            print(charactername.strip("\n"), "- What?")
            time.sleep(2)
            print("Zane - I stopped by your house earlier...")
            print("\n1 ) WHAT DID YOU DO?")
            while 1:
                input7 = input("> ")
                if input7 == "1":
                    break
                else:
                    print("Invalid Input, Please Try Again...")
            time.sleep(1)
            print("Zane - I well, you know. Put an explosive in your boiler.")
            time.sleep(2)
            print("\n1 ) Your Lying!\n2 ) Dont you even think about it...")
            while 1:
                input8 = input("> ")
                if input8 == "1":
                    print(charactername.strip("\n"), "- Your Lying!")
                    time.sleep(2)
                    print("Zane pulls out a detonator")
                    time.sleep(2)
                    print("Zane - Lying Now, Hahahahaha")
                    break
                elif input8 == "2":
                    print(charactername.strip("\n"), "- Dont you even think about it...")
                    time.sleep(2)
                    print("Zane pulls out a detonator")
                    time.sleep(2)
                    print("Zane - And whys that?")
                    print("\n1 ) Truth\n2 ) Lie")
                    while 1:
                        input9 = input("> ")
                        if input9 == "1":
                            print(charactername.strip("\n"), "- Look I dont have anything at home but that house means so much to me, please dont do it...")
                            time.sleep(2)
                            print("Zane - Hmmm...")
                            break
                        elif input9 == "2":
                            print(charactername.strip("\n"), "- I have a pet Elephant at home, Please dont do this...")
                            time.sleep(2)
                            print("Zane - Really? Well I will take that in to consideration ;/")
                            break
                        else:
                            print("Invalid Input, Please enter 1 or 2...")
                    break
                else:
                    print("Invalid Input, Please Enter 1 or 2...")
            time.sleep(2)
            print("Zane - I tell you what...")
            time.sleep(2)
            print("\n1 ) What?")
            while 1:
                input10 = input("> ")
                if input10 == "1":
                    break
                else:
                    print("Invalid Input, Please Try Again...")
            time.sleep(2)
            print("Zane - Pass me all your gold, And I wont destroy it...")
            time.sleep(2)
            print("\n1 ) Give Zane All Gold\n2 ) Dont Give It")
            while 1:
                input11 = input("> ")
                if input11 == "1":
                    gold = 0
                    time.sleep(2)
                    print("Zane snatches all the gold from your hands")
                    time.sleep(2)
                    print("Zane decides to destroy your house anyways..., It has been removed from the map...")
                    for i in range(len(array)):
                        for l in range(len(array[i])):
                            if array[i][l] == "H":
                                findingArray2.append(i)
                                findingArray2.append(l)

                    array[findingArray2[0]][findingArray2[1]] = " "
                    time.sleep(3)
                    break
                elif input11 == "2":
                    time.sleep(2)
                    print("Your house gets destroyed, It has been removed from the map...")
                    for i in range(len(array)):
                        for l in range(len(array[i])):
                            if array[i][l] == "H":
                                findingArray2.append(i)
                                findingArray2.append(l)

                    array[findingArray2[0]][findingArray2[1]] = " "
                    time.sleep(3)
                    break
                else:
                    print("Invalid Input, Please Try Again...")
        else:
            print("Invalid Input, Please Try Again...")
            continue

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        time.sleep(2)
        print("Zane runs away out of town...")
        time.sleep(5)
        f.close()
        gold = int(gold)
        charactername = charactername.strip("\n")
        f = open("data.txt", "w")
        f.write("charactername=")
        f.write(charactername)
        f.write("\n")
        f.write("gold=")
        f.write('%d' % gold)
        f.write("\n")
        f.write("lives=")
        f.write('%d' % lives)
        f.write("\n")
        f.close()
        # Removing zane from the map
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "Z":
                    findingArray.append(i)
                    findingArray.append(l)

        array[findingArray[0]][findingArray[1]] = " "

        with open("map.csv", "w", newline="") as c:
            csvWriter = csv.writer(c, delimiter=',')
            csvWriter.writerows(array)
        print("Data Saved, Returning To Main Game")
        play()

def house():
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

    ) )        /\
   =====      /  \
  _|___|_____/ __ \____________
 |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|
 |_________|  ____  |__________|
  | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||
  ||--+---|| |    | ||---+---||
  ||__|___|| |   o| ||___|___||
  |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;;""")

    print("Welcome home", charactername.strip("\n"), ", Please select an option to continue:\n1 ) Give Game Feedback\n2 ) Game Credits\n3 ) Leave House")
    while 1:
        input1 = input("> ")
        if input1 == "1":
            rating = 0
            tmp = open("feedback.txt", "a")
            tmp.close()
            print("How would you rate the game overall: (Out Of 5)")
            while 1:
                input2 = input("> ")
                if input2 == "0":
                    rating = 0
                    break
                elif input2 == "1":
                    rating = 1
                    break
                elif input2 == "2":
                    rating = 2
                    break
                elif input2 == "3":
                    rating = 3
                    break
                elif input2 == "4":
                    rating = 4
                    break
                elif input2 == "5":
                    rating = 5
                    break
                else:
                    print("Invalid Input, Please enter a number 1-5...")
            print("How did you find the story (Text Answer):")
            input3 = input("> ")
            print("Would you recommend this game to a friend? (Yes or No)")
            while 1:
                input4 = input("> ").upper()
                if input4 == "YES":
                    recommendToFriend = "Yes"
                    break
                elif input4 == "NO":
                    recommendToFriend = "No"
                    break
                else:
                    print("Invalid Input, Please enter Yes or No.")
            print("Any Additional Notes (Text Answer):")
            input5 = input("> ")
            fb = open("feedback.txt", "w")
            fb.write("overallRating=")
            fb.write('%d' % rating)
            fb.write("\n")
            fb.write("howFoundStory=")
            fb.write(input3)
            fb.write("\n")
            fb.write("recommendToFriend=")
            fb.write(recommendToFriend)
            fb.write("\n")
            fb.write("additionalNotes=")
            fb.write(input5)
            fb.close()
            time.sleep(3)
            print("\nThank you for taking part in the survey, It has been saved and sent to the Game Developer.")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Please select an option to continue:\n1 ) Give Game Feedback\n2 ) Game Credits\n3 ) Leave House")
        elif input1 == "2":
            print("""
█████████████████████████████████████████
█─▄▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█▄─▄█─▄─▄─█─▄▄▄▄█
█─███▀██─▄─▄██─▄█▀██─██─██─████─███▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀""")
            time.sleep(2)
            print("\nGame Developer:")
            time.sleep(0.5)
            print("Tristan")
            time.sleep(2)
            print("\nGame Ideas:")
            time.sleep(0.5)
            print("Zane")
            time.sleep(0.5)
            print("AJ")
            time.sleep(0.5)
            print("Markus")
            time.sleep(2)
            print("\nDevelopment Support:")
            time.sleep(0.5)
            print("AJ")
            time.sleep(5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Please select an option to continue:\n1 ) Give Game Feedback\n2 ) Game Credits\n3 ) Leave House")
        elif input1 == "3":
            print("Leaving Home.")
            time.sleep(1)
            print("Leaving Home..")
            time.sleep(1)
            print("Leaving Home..")
            time.sleep(1)
            f.close()
            gold = int(gold)
            charactername = charactername.strip("\n")
            f = open("data.txt", "w")
            f.write("charactername=")
            f.write(charactername)
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
            print("Invalid Input, Please enter 1, 2 or 3...")

def greg():
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
░██████╗░██████╗░███████╗░██████╗░
██╔════╝░██╔══██╗██╔════╝██╔════╝░
██║░░██╗░██████╔╝█████╗░░██║░░██╗░
██║░░╚██╗██╔══██╗██╔══╝░░██║░░╚██╗
╚██████╔╝██║░░██║███████╗╚██████╔╝
░╚═════╝░╚═╝░░╚═╝╚══════╝░╚═════╝░""")

    print("Hello", charactername.strip("\n"), ", Ive been looking to meet you for a while...")
    print("\n1 ) How do you know my name?\n2 ) What do you want?")
    while 1:
        input1 = input("> ")
        if input1 == "1":
            print(charactername.strip("\n"), "- How do you know my name?")
            time.sleep(3)
            print("Greg - The bartender told me, he kinda knows everything from around here...")
            break
        elif input1 == "2":
            print(charactername.strip("\n"), "- What do you want?")
            time.sleep(3)
            print("Greg - Well its not necessarily what I want, I more have something to give you...")
            break
        else:
            print("Invalid Input, Please enter 1 or 2...")

    time.sleep(2)
    print("Greg - Heres the gold for getting those clowns out of here, on behalf of the bartender of course...")
    time.sleep(1)
    print("+250 Gold")
    gold = gold + 250
    time.sleep(3)
    print("Greg - I also have something else for you, Were looking to build a new bridge to the next town...")
    time.sleep(3)
    print("Greg - Well... Those thugs destroyed it on their way out...")
    time.sleep(3)
    print("Greg - Cut down about 4 trees and I will give you 50 gold for each one, after that look for my friend Sam...")
    time.sleep(3)
    print("\n1 ) Accept and Leave")
    while 1:
        input2 = input("> ")
        if input2 == "1":
            break
        else:
            print("Invalid Input, Please Try Again...")
    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # Removing greg from the map
    array = [[0] * 25 for _ in range(10)]
    findingArray = []
    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]

    for i in range(len(array)):
        for l in range(len(array[i])):
            if array[i][l] == "G":
                findingArray.append(i)
                findingArray.append(l)

    array[findingArray[0]][findingArray[1]] = " "
    runtimes = 0
    while 1:
        a = random.randrange(1, 9)
        b = random.randrange(1, 24)
        if array[a][b] == " ":
            array[a][b] = "T"
            runtimes = runtimes + 1
            if runtimes >= 4:
                break
    while 1:
        a = random.randrange(1, 9)
        b = random.randrange(1, 24)
        if array[a][b] == " ":
            array[a][b] = "S"
            break

    with open("map.csv", "w", newline="") as c:
        csvWriter = csv.writer(c, delimiter=',')
        csvWriter.writerows(array)
    time.sleep(1)
    print("Greg disappears into one of the nearby houses...")
    f.close()
    gold = int(gold)
    charactername = charactername.strip("\n")
    f = open("data.txt", "w")
    f.write("charactername=")
    f.write(charactername)
    f.write("\n")
    f.write("gold=")
    f.write('%d' % gold)
    f.write("\n")
    f.write("lives=")
    f.write('%d' % lives)
    f.write("\n")
    f.close()
    print("Data Saved, Returning To Main Game")
    time.sleep(3)
    play()

def sam():
    judgement = 0
    array = [[0] * 25 for _ in range(10)]

    with open("map.csv", "r") as c:
        reader = csv.reader(c)
        array = [row for row in reader]

    while 1:
        for i in range(len(array)):
            for l in range(len(array[i])):
                if array[i][l] == "T":
                    judgement = judgement + 1
                    break

        if judgement <= 0:
            print("""
┏━━━┳━━━┳━┓┏━┓
┃┏━┓┃┏━┓┃┃┗┛┃┃
┃┗━━┫┃╋┃┃┏┓┏┓┃
┗━━┓┃┗━┛┃┃┃┃┃┃
┃┗━┛┃┏━┓┃┃┃┃┃┃
┗━━━┻┛╋┗┻┛┗┛┗┛""")
            print("\nHello, Im Sam... What can I do for you?\n1 ) Greg Told Me To Talk To You...")
            while 1:
                input1 = input("> ")
                while 1:
                    if input1 == "1":
                        print("Sam - ")
                    else:
                        print("Invalid Input, Please Try Again...")
        else:
            print("\nYou have not collected all trees yet...\n")
            time.sleep(2)
            print("Returning to map.")
            time.sleep(1)
            print("Returning to map..")
            time.sleep(1)
            print("Returning to map...")
            time.sleep(1)
            play()

if __name__ == "__main__":
    main()
