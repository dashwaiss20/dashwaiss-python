class Petclass():
    def __init__(self, vType, vName, vBreed):
        self.type = vType
        self.name = vName
        self.breed = vBreed

    def getType(self):
        return(self.type)
    def getName(self):
        return(self.name)
    def getBreed(self):
        return(self.breed)
    def whatIsIt(self):
        print('My Pet is a ' + Pet1.type + " Thier name is " + Pet1.name + " The breed is a " + Pet1.breed)
    def whatIsIt2(self):
        print('My Pet is a ' + Pet2.type + " Thier name is " + Pet2.name + " The breed is a " + Pet2.breed)

Pet1 = Petclass('Dog', 'Kaiser', 'Pure Bread German Shapherd')

Pet1.whatIsIt()

Pet2 = Petclass('Cat', 'Devil', 'sphynx cat')

Pet2.whatIsIt2()

class myCage():
    def __init__(self, vType, vDanger, vBreed):
        self.type = vType
        self.breed = vBreed
        self.danger = vDanger

    def getType(self):
        return(self.type)
    def getDanger(self):
        return(self.danger)
    def getBreed(self):
        return(self.breed)
    def whatdanger(self):
        if self.danger == 'True':
            return('dangerous')
        elif self.danger == 'False':
            return ('not dangerous')
    def whatIsIt3(self):
        print('My Pet is a ' + Pet3.type + " They are " + Pet3.whatdanger() + " The breed is a " + Pet3.breed)
        print('My Pet is a ' + Pet4.type + " They are " + Pet4.whatdanger() + " The breed is a " + Pet4.breed)

Pet3 = myCage('Snake', 'True', 'King Cobra')
Pet4 = myCage('Rat', 'False', 'King Cobra')








Pet3.whatIsIt3()
