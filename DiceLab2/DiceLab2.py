from random import *

def dice():
    loop = "y"
    blank = '|       |'
    onedot ='|   *   |'
    twodot ='|  * *  |'
    topBot = "---------"
    Dice1 = [topBot, blank, onedot, blank, topBot]
    Dice2 = [topBot, blank, twodot, blank, topBot]
    Dice3 = [topBot, onedot, onedot, onedot, topBot]
    Dice4 = [topBot, twodot, blank, twodot, topBot]
    Dice5 = [topBot, twodot, onedot, twodot, topBot]
    Dice6 = [topBot, twodot, twodot, twodot, topBot]
    yoinks = [Dice1,Dice2,Dice3,Dice4,Dice5,Dice6]

    times = 0
    while loop== "y":
        times = times + 1
        y = randnum()
        print(whichDice(randnum, yoinks, dicea))
        print ('you rolled a ' + str(y))
        loop = input('would you like to play again (y/n)')
        print('you have played ' + str(times) + " times")

def randnum():
    x = randint(1,6)
    return(x)

def whichDice(randnum, yoinks):
    if randnum == 1:
        dicea = yoinks[0]
    if randnum == 2:
        dicea = yoinks[1]
    if randnum == 3:
        dicea = yoinks[2]
    if randnum == 4:
        dicea = yoinks[3]
    if randnum == 5:
        dicea = yoinks[4]
    if randnum == 6:
        dicea = yoinks[5]

    return(dicea)
dice()















    # if randnum2 == 1 or randnum == 2:
    #     bb = yoinks[0]
    # elif randnum2 == 3:
    #     bb = yoinks[1]
    # elif randnum2 == 4 or randnum == 5 or randnum == 6:
    #     bb = yoinks[2]
    #
    # if randnum2 == 1 or randnum == 3 or randnum == 5:
    #     cc = yoinks[1]
    # elif randnum2 == 4:
    #     cc = yoinks[0]
    # elif randnum2 == 2 or randnum == 6:
    #     cc = yoinks[2]
    #
    # if randnum2 == 1 or randnum == 2:
    #     dd = yoinks[0]
    # elif randnum2 == 3:
    #     dd = yoinks[1]
    # elif randnum2 == 4 or randnum == 5 or randnum == 6:
    #     dd = yoinks[2]

    # if randnum == 1 or randnum == 2:
    #     b = yoinks[0]
    # elif randnum == 3:
    #     b = yoinks[1]
    # elif randnum == 4 or randnum == 5 or randnum == 6:
    #     b = yoinks[2]
    #
    # if randnum == 1 or randnum == 3 or randnum == 5:
    #     c = yoinks[1]
    # elif randnum == 4:
    #     c = yoinks[0]
    # elif randnum == 2 or randnum == 6:
    #     c = yoinks[2]
    #
    # if randnum == 1 or randnum == 2:
    #     d = yoinks[0]
    # elif randnum == 3:
    #     d = yoinks[1]
    # elif randnum == 4 or randnum == 5 or randnum == 6:
    #     d = yoinks[2]





