def main():
    num = int(input('how many? '))
    l = [0] * num
    for s in range(0, num):
        l = input('grade')
    length = len(l)
    print('Bellarmine point grade average')
    gradelevel = input('what grade are you in? ')
    print('congrats you are ' + str(yearInSchool(gradelevel)))
    calcGPA = getGPA(l, length)
    grade = getlettergrade(calcGPA)
    print('you GPA is ' + str(calcGPA))
    print('your current letter grade is ' + str(grade))
    if grade == ('D') or grade == ('F'):
        print('you failed')
    else:
        print('you passed')


def yearInSchool(gradelevel):
    if gradelevel == 9:
        longGrade = ('a Freshman')
    elif gradelevel == 10:
        longGrade = ('a Sophmore')
    elif gradelevel == 11:
        longGrade = ('a Junior')
    elif gradelevel == 12:
        longGrade = ('a Senior')
    else:
        longGrade = ('not in Highschool')
    return (longGrade)

def getGPA(myL,length):
#    gpa = sum(myL) / float(MyLength)
    #gpa = float("0")
    added = 0.0
    for x in myL:
        added += float(x)
    gpa = (added) / int(length)
    return (gpa)

#gpa = float(gpa + (x))
#gpa = ((gpa) / len(myL))

def getlettergrade(getGPA):
    if getGPA >= 90:
        lettergrade = ('A')
    elif getGPA >= 80:
        lettergrade = ("B")
    elif getGPA >= 70:
        lettergrade = ("C")
    elif getGPA >= 60:
        lettergrade = ("D")
    else:
        lettergrade = ("F")
    return (lettergrade)

main()
