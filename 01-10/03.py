# 13195 prime fakor = 5 , 7, 13, 29
import math
prims = []


def primTest(p):
    for i in range(2,int(math.sqrt(p))+1):
        if p % i == 0:
            #print("keine prim " , p)
            return False
    return True


def findPrim(number):  # 10

    for i in range(2,int(math.sqrt(number))+1):

        if primTest(i) and number % i == 0:
            prims.append(i)

    print(prims)





findPrim(600851475143)

