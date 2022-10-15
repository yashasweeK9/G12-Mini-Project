import lib 
import math

SQRT5 = math.sqrt(5)
PHI = (SQRT5+1)/2

def isFibonacci(number):
    number = int(number)
    exp1 = (5*number*number)+4
    exp2 = (5*number*number)-4
    return lib.isPerfectSquare(exp1) or lib.isPerfectSquare(exp2)

def getNthFibonacci(N): #Binet's Formula

    answer = round(((PHI**N)-((-PHI)**(-N)))/SQRT5)
    return int(answer)

def getFibonacciIndex(number):
    number = int(number)
    if(number==0):
        return 0
    if(number==1):
        return [1,2]
    index = round(2.078087 * math.log(number) + 1.672276)
    return int(index)

# Takes a fibonacci number that isn't 
def getNearestTerm(number):
    return getNthFibonacci(getFibonacciIndex(number)+1)

def getRightNeighbour(number):
    number = int(number)
    if (number!=1):
        return getNthFibonacci(getFibonacciIndex(number)+1)
    else:
        return getNthFibonacci(3)


def getReference(number):
    return number

def getLeftNeighbour(number):
    number = int(number)
    index = getFibonacciIndex(number)
    if(number!=1):
        if index==0:
            return "START"
        return getNthFibonacci(index-1)
    else:
        return getNthFibonacci(0)

def getSequence(N):
    sequence = ""
    initA = 0
    initB = 1
    sum = 0
    for index in range(0,N+1):
        sequence+=str(sum)+" , "
        initA = initB
        initB = sum
        sum = initA+initB
    return sequence[0:-3].strip()
