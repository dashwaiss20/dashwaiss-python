from random import *
def dice () :
    loop = 'y'
    times = 0
    while loop=='y' :
        times = times + 1
        y = randNum ()
        x = randNum ()
        print(whichDice(y , x))
        print ("You rolled a - " + str(y) + " and " + str(x) + ".")
        print ("You have played " + str(times) + " times.")
        loop = input ("Would you like this to run again? (y/n) - ")
def randNum () :
    z = randint(1,6)
    return (z)


def whichDice (x , y) :
    a = ' -------   ------- '
    if x==1 or x==2 :
        ba = '|       |'
    elif x==3 :
        ba = '|   *   |'
    elif x==4 or x==5 or x==6 :
        ba = '| *  *  |'

    if x==1 or x==3 or x==5 :
        ca = '|   *   |'
    elif x==4 :
        ca = '|       |'
    elif x==2 or x==6 :
        ca = '| *  *  |'

    if x==1 or x==2 :
        da = '|       |'
    elif x==3 :
        da = '|   *   |'
    elif x==4 or x==5 or x==6 :
        da = '| *  *  |'

    if y==1 or y==2 :
        bb = ' |       |'
    elif y==3 :
        bb = ' |   *   |'
    elif y==4 or y==5 or y==6 :
        bb = ' | *  *  |'

    if y==1 or y==3 or y==5 :
        cb = ' |   *   |'
    elif y==4 :
        cb = ' |       |'
    elif y==2 or y==6 :
        cb = ' | *  *  |'

    if y==1 or y==2 :
        db = ' |       |'
    elif y==3 :
        db = ' |   *   |'
    elif y==4 or y==5 or y==6 :
        db = ' | *  *  |'

    b = ba + bb
    c = ca + cb
    d = da + db
    return(a + "\n" + b + "\n" + c + "\n" + d + "\n" + a)

dice ()


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





