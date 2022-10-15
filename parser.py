from fibonacci import getSequence
from lib import *

def parseInput(usrInp):
    tokens = usrInp.split(" and ")
    return tokens

def validateInput(usrToken):
    try:
        usrToken = int(usrToken)
        if(usrToken<0 or usrToken>getMaxIntegerValue()):
            return [False,">>> {} is Out of Range from Integer Scope i.e. [0,{}]".format(usrToken,getMaxIntegerValue())]
        return [True]
    except:
        return [False,">>> {} is not recognized as a Valid Input".format(usrToken)]


def notifyExistence(number,result):
    if(result):
        return ">>> EXIST?    : {} does Exists in the Fibonacci Series".format(number)
    else:
        return ">>> EXIST?    : {} does NOT Exists in the Fibonacci Series".format(number)

def notifyIndex(index):
    str = ""
    catStr = "i.e. @index:: {}".format(index)
    if(index!=0):
        str = ">>> INDEX     : ... {} ... ".format(index)+catStr
    else:
        str = ">>> INDEX     : {} ... ".format(index)+catStr
    return str

def notifyNeighbour(leftNeighbour,ref,rightNeighbour):
    if int(ref) == 1:
        return ">>> NEIGHBOUR : START , {} , {} , {} , {} ...".format(leftNeighbour,ref,ref,rightNeighbour) 
    if leftNeighbour == "START":
        return ">>> NEIGHBOUR : {} , {} , {} ...".format(leftNeighbour,ref,rightNeighbour)    
    return ">>> NEIGHBOUR : ... {} , {} , {} ...".format(leftNeighbour,ref,rightNeighbour)

def displaySequence(range):
    if(type(range)==type([0,1])):
        return ">>> SEQUENCE  : "+getSequence(2)    
    return ">>> SEQUENCE  : "+getSequence(range)
