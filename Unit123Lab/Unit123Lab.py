def main():
    print('Bellarmine point grade average')
    gradeLevel = input('what grade are you in? ')
    print ("You are in " + str(yearInSchol(gradeLevel)))







def yearInSchool(gradeLevel):
    if gradeLevel == 9:
        longGrade = ('Freshman')
    elif gradeLevel == 10:
        longGrade = ('Sophmore')
    elif gradeLevel == 11:
        longGrade = ('Junior')
    elif gradeLevel == 12:
        longGrade = ('Senior')
    else:
        longGrade = ('no grade')
    return (longGrade)




main()


