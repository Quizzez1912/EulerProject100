import math
#sol 906609
# 998.001 999x999
match = 0
found = False
number1 = str(91)
number2 = str(99)
number3 = str(1224)


def primTest(p):
    for i in range(2,int(math.sqrt(p))+1):
        if p % i == 0:
            #print("keine prim " , p)
            return False
    return True


def findPalin():
    global match
    for j in range(100000, 998001):
        for i in range(len(str(j))//2):
            lenminus = len(str(j)) - 1
            numberA = str(j)[i]
            numberB = str(j)[lenminus-i]

            #print(numberA)
           # print(numberB)
            #print("")

            if numberA == numberB:
               # print("same")
               # print(j)
                match += 1

            if match == 3 and j % 3 == 0:
                print("found it ", j)


        match = 0




findPalin()

