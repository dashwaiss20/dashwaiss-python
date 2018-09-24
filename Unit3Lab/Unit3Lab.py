def myfunc() :
    print('Python')
    print('St. Charles')
myfunc()

def grade():
    x =input('what Grade are you in ')
    y=int(x) - 1
    print(str(y))
grade()

def helloCity(city, grade):
    print('you are from ' + city)
    print('you are in ' + str(grade))

print('starts here')
myCity = input('where are you from? ')
myGrade = input('what grade are you in? ')
helloCity(myCity, myGrade)

from random import *

def RandomNumber():
    x = input('what is your start number? ')
    y = input('what is your end number? ')
    myNumber = randint(int(x), int(y))
    print(str(myNumber) + ' is a number between ')
    print(str(x) + " and " +str(y))

RandomNumber()



def areabox(length,width):
    area=(int(length)*int(width))
    return(area)

def permofbox(length,width):
    perm=2*(int(length))+2*(int(width))
    return(perm)

x=input('what is the length of your box? ')
y=input('what is the width of your box? ')
print('the area of your box is '+ str(areabox(x,y)))
print('the perimeter of your box is ' + str(permofbox(x,y)) )

def multiply(Times,list):
    nL = [0] * 4
    nL [0] = L [0] * Times
    nL [1] = L [1] * Times
    nL [2] = L [2] * Times
    nL [3] = L [3] * Times
    return (nL)
L = [1,2,3,4]
print('your list is '+str(L) + " Your list times 2 is " + str((multiply(2, [1,2,3,4]))) + (' your list times 3 is ') + str((multiply(3, [1,2,3,4]))) + ".")
