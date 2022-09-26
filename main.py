INCREMENT = 1024
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
    while(True):
        for number in numbers:
            userNumber = input()
            if(userNumber == number):
                continue
            else:
                failedBool = False
                break
        if(failedBool == False):
            break
        else:
            place += 1
            numbers = getMoreNumbers(place)
CMDmain()