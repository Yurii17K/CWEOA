from sum_alg import sumAlg
from diff_alg import diffAlg, isBigger
from utils_alg import *

def divAlgB10(dividend, divisor):
    # no idea how and why but for insanely large numbers it happened once, so here's an error
    if isEqual(divisor, 0):
        raise ValueError("CAN NOT DIVIDE BY ZERO")
    if isEqual(str(dividend)[0], '-'):
        return divWithNeg(str(dividend), divisor)
    return divAlg(dividend, divisor, 10)

def divAlg(dividend, divisor, base):
    if (isSmaller(dividend, divisor)):
        return (0, int(dividend))

    dividend = list(str(dividend))
    divisor = str(divisor)
    reminder = 0
    res = ""

    dividendLen = len(dividend)

    dividendStartPointer = 0
    dividendEndPointer = 0
    while (isSmaller(dividendEndPointer, dividendLen)):

        # iterate over a dividend until a number bigger or equal to the divisor is found
        if(isSmaller(''.join(dividend[dividendStartPointer:dividendEndPointer + 1]), divisor)):
            reminder = int(''.join(dividend[dividendStartPointer:dividendEndPointer + 1]))

            # if a devisor is too small and this is not a first lookup and a 0 (obviously don't add 0s when dividing 1003 by 127 in the beginning just because 1,10,100 are smaller)
            if (not isEqual(dividendStartPointer, 0)):
                res += '0'
        else:
            tmpDividend = int(''.join(dividend[dividendStartPointer:dividendEndPointer + 1]))
            reminder = 0
            tmpSum = 0

            # perform internal division
            for multiplications in range(20): # divisors can't be larger than 9, but just to be safe in this crazy world
                if (isSmaller(tmpSum, tmpDividend)):
                    tmpSum = sumAlg(tmpSum, divisor, base)
                else:
                    if (isBigger(tmpSum, tmpDividend)): 
                        multiplications = diffAlg(multiplications, 1, base=10)
                        tmpSum = diffAlg(tmpSum, divisor, base)
                    res += str(multiplications)
                    reminder = diffAlg(tmpDividend, tmpSum, base)
                    dividend[dividendEndPointer] = str(reminder)
                    dividendStartPointer = dividendEndPointer
                    break
        
        # increase pointer
        dividendEndPointer = sumAlg(dividendEndPointer, 1, base=10)
   
    return (int(res), reminder)
    
def divWithNeg(divident, divisor):
    multiplications = 0
    tmpSum = 0
    nonNegDivident = int(str(divident[1:]))
    reminder = 0
    while(isSmaller(tmpSum, nonNegDivident)):
        multiplications += 1
        tmpSum += divisor
    
    return (int('-' + str(multiplications)), diffAlg(tmpSum, nonNegDivident, 10))

# print(divAlg(-14, 71, 10))