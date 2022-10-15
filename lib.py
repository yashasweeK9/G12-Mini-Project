import sys
def isPerfectSquare(number):
    root = int(number**0.5)
    return number == (root**2)

def getMaxIntegerValue():
    return sys.maxsize

def askInput():
    usrInp = input("[INPUT] : ").strip()
    return usrInp