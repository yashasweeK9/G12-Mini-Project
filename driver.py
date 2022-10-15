from fibonacci import * 
from lib import *
from parser import *

usrInput = askInput()
tokenlist = parseInput(usrInput)
tokens = len(tokenlist)

if(tokens==0):
    print("NO INPUT RECOGNIZED")
else:
    for value in tokenlist:
        info = validateInput(value)
        if(info[0]):
            isFibo = isFibonacci(value)
            print(notifyExistence(value,isFibo))
            if(isFibo):
                index = getFibonacciIndex(value)
                print(notifyIndex(index))
                print(notifyNeighbour(getLeftNeighbour(value),getReference(value),getRightNeighbour(value)))
                print(displaySequence(index))
        else:
            print(info[-1])
        print()