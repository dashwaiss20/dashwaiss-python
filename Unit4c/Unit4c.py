def main():
    draw7()
    print('stars')
    starsandStripes()
    print('pause')
    incTriangle()
def draw7():
    string = ''
    for i in range(0,7):
        string = ''
        for i in range(0,7):
            string += "*"
        print (string)

def starsandStripes():
    for i in range(0,3):
        for a in range(0,7):
            print("*", end = '')
        print("")
        for x in range(0,7):
            print("-", end = '')
        print('')

def incTriangle():
    for i in range(1,8):
        for j in range(0,i):
            print(i, end = '')
        print()

main()
