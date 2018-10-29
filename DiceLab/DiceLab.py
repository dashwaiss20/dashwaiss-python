from random import *

def dice():
    loop = "y"
    times = 0
    while loop== "y":
        times = times + 1
        y = randnum()
        print(whichDice(y))
        print ('you rolled a ' + str(y))
        loop = input('would you like to play again (y/n)')
        print('you have played ' + str(times) + "timesy")

def randnum():
    x = randint(1,6)
    return(x)

def whichDice(randnum):
    a = "---------"
    e = "---------"
    if randnum == 1 or randnum == 2:
        b = '|       |'
    elif randnum == 3:
        b = '|   *   |'
    elif randnum == 4 or randnum == 5 or randnum == 6:
        b = '|  * *  |'

    if randnum == 1 or randnum == 3 or randnum == 5:
        c = '|   *   |'
    elif randnum == 4:
        c = '|       |'
    elif randnum == 2 or randnum == 6:
        c = '|  * *  |'

    if randnum == 1 or randnum == 2:
        d = "|       |"
    elif randnum == 3:
        d = "|   *   |"
    elif randnum == 4 or randnum == 5 or randnum == 6:
        d = "|  * *  |"

    return(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e)

dice()



