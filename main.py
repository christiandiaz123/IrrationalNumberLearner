INCREMENT = 1024
import json

try:
    highScoreHTable = json.load("High_Scores.json")
except:
    print("ran")
    with open("High_Scores.json", 'w') as file:
        file.write("{\n}")
    highScoreHTable = dict()


def getMoreNumbers(place: int, txtFileName: str):
    # TODO find a way to generate an infinite amount of numbers and not just the 1000000 that are in the text file
    with open(txtFileName, 'r') as file:
        file.seek(place * INCREMENT)
        PIString = file.read(INCREMENT)
        PIList = list(PIString)
        return PIList


def CMDmain():
    print("Please input the irrational number you'd like to memorize:")
    with open("Irrationals.json", "r") as file:
        irrationalHTable = json.load(file)
    for key, val in irrationalHTable.items():
        print(f"{key}. {val}")
    while(True):
        num = input("Please input the number(int) you want to practice\n")
        try:
            numBoolean = num in irrationalHTable.keys()
        except:
            continue
        if(numBoolean):
            break
    with open("IrrationalFileNames.json", "r") as file:
        IrrationalFilesTexts = json.load(file)
    txtFileName = IrrationalFilesTexts[num]
    place = 0
    numbers = getMoreNumbers(place, txtFileName)
    failedBool = True
    try:
        highScore = highScoreHTable[txtFileName]
    except:
        highScoreHTable[txtFileName] = 0
        highScore = highScoreHTable[txtFileName]
    while (True):
        count = 0
        for number in numbers:
            userNumber = input()
            if (userNumber == number):
                count += 1
                continue
            else:
                failedBool = False
                break
        if (failedBool == False):
            break
        else:
            place += 1
            numbers = getMoreNumbers(place, txtFileName)
    print(f"Score: {count}")
    if (count > highScore):
        highScoreHTable[txtFileName] = count
        print(highScoreHTable)
        with open("High_Scores.json", 'w') as file:
            json.dump(highScoreHTable, file)
        print("New High Score")


CMDmain()
# TODO Unit Tests
# TODO GUI
# TODO Other Irrational Numbers
