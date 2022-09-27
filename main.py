INCREMENT = 1024
import json

try:
    highScoreHTable = json.load("High_Scores.json")
except:
    with open("High_Scores.json", 'w') as file:
        file.write("{\n}")
    highScoreHTable = dict()
def getMoreNumbers(place: int):
    with open("PI_DIGITS.txt", 'r') as file:
        file.seek(place*INCREMENT)
        PIString = file.read(INCREMENT)
        PIList = list(PIString)
        return PIList
def CMDmain():
    place = 0
    numbers = getMoreNumbers(place)
    failedBool = True
    try:
        highScore = highScoreHTable["PI_DIGITS.txt"]
    except:
        highScoreHTable["PI_DIGITS.txt"] = 0
        highScore = highScoreHTable["PI_DIGITS.txt"]
    while(True):
        count = 0
        for number in numbers:
            userNumber = input()
            if(userNumber == number):
                count += 1
                continue
            else:
                failedBool = False
                break
        if(failedBool == False):
            break
        else:
            place += 1
            numbers = getMoreNumbers(place)
    print(f"Score: {count}")
    if(count>highScore):
        highScoreHTable["PI_DIGITS.txt"] = count
        with open("High_Scores.json", 'w') as file:
            json.dump(highScoreHTable, file)
        print("New High Score")
CMDmain()
#TODO Unit Tests
#TODO GUI
#TODO Other Irrational Numbers
