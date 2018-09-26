def main():
    l = [86.5, 75.3, 98.9, 92.3]
    print('Bellarmine point grade average')
    gradeLevel = input('what grade are you in? ')
    print ("congrats You are " + str(yearInSchool(gradeLevel)))
    print("your current GPA is a ") + str(getGPA(l))
    print("your current letter grade is a ") + str(getlettergrade(getGPA(l)))

def yearInSchool(gradeLevel):
    if gradeLevel == 9:
        longGrade = ('a Freshman')
    elif gradeLevel == 10:
        longGrade = ('a Sophmore')
    elif gradeLevel == 11:
        longGrade = ('Junior')
    elif gradeLevel == 12:
        longGrade = ('a Senior')
    else:
        longGrade = ('no grade')
    return (longGrade)

def getGPA(l):
    l = [86.5, 75.3, 98.9, 92.3]
    gpa = sum(l) / float(len(l))
    return(gpa)

def getlettergrade(getGPA):
    if getGPA >= 90:
        lettergrade = ("A")
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


