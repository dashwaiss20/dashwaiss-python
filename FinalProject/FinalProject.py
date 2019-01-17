import random

def starting_Character():
    print('-----------------------------------')
    print('Hello! Welcome To The Oregon Trail.')
    print('-----------------------------------')
    Name = input('What would you like your name to be? ')
    print('Hello ' + (Name))

starting_Character()


river = input('you reach a river do you try to cross it? [y/n] ')


yeet = random.randint(1,101)

if river == ('y') or ('yes'):
    if yeet >= (80):
        print('you died')
#    if yeet <= (79):
#       print('you survived')
if river == ('no') or ('n'):
    print(river)
    input('pause')
    no_river = random.randint(1,11)
    if no_river >= (9):
        print('you start to starve.')
    elif no_river <= (8):
        print('you are ')

