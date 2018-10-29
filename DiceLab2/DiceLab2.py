from random import *

def dice():
    loop = "y"
    yoinks = ['|       |' , '|   *   |' , '|  * *  |']
    times = 0
    while loop== "y":
        times = times + 1
        y = randnum()
        print(whichDice(y,yoinks))
        print ('you rolled a ' + str(y))
        loop = input('would you like to play again (y/n)')
        print('you have played ' + str(times) + "times")

def randnum():
    x = randint(1,6)
    return(x)

def whichDice(randnum , yoinks):
    a = "---------"
    e = "---------"

    if randnum == 1 or randnum == 2:
        b = yoinks[0]
    elif randnum == 3:
        b = yoinks[1]
    elif randnum == 4 or randnum == 5 or randnum == 6:
        b = yoinks[2]

    if randnum == 1 or randnum == 3 or randnum == 5:
        c = yoinks[1]
    elif randnum == 4:
        c = yoinks[0]
    elif randnum == 2 or randnum == 6:
        c = yoinks[2]

    if randnum == 1 or randnum == 2:
        d = yoinks[0]
    elif randnum == 3:
        d = yoinks[1]
    elif randnum == 4 or randnum == 5 or randnum == 6:
        d = yoinks[2]




    return(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e)

dice()



