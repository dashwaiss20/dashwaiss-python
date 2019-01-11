import random

def starting_Character():
    Name = input('What would you like your name to be? ')
    print('Hello ' + (Name))

starting_Character()

def Starting_Game():

    print('[meat], [gun], [axle], [wheel]')
    jkjk = input('what would you like to buy?')
    print(jkjk)
    if jkjk == ('wheel'):
        amountW = input('how many would you like to buy?')
        if amountW == ('1'):
            print("1 wheel")
        if amountW == ('2'):
            print("2 wheels")
        if amountW == ('3'):
            print("3 wheels")
        if amountW == ('4'):
            print("4 wheels")
        if amountW == ("5"):
            print('5 wheels')
        else:
            print('oofofofo')

    Inventory  =  ['yeet', ('s')]
    print(Inventory)

Starting_Game()
