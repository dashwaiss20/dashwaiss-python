numlist=[1,2,3,4,5,6,7,8,9,10]
print(numlist)
print(len(numlist))
print(numlist[0])
print(numlist[9])
sublist1=numlist[0:5]
print(sublist1)
sublist1.insert(0,29)
print(sublist1)
sublist1.append(9)
print(sublist1)
sublist2=sublist1 + [30]
print(sublist2)
myClasses=['Math','English','Spanish','History','Python','Chemistry','Team Sports']
myClasses.remove('Chemistry')
print(myClasses)
favClass=myClasses.pop(4)
print('My Favorite class is '+favClass)
