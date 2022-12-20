from sum_alg import sumAlg
from diff_alg import diffAlg, isBigger
from utils_alg import *

def divAlg(dividend, divisor, base):
    if (isSmaller(dividend, divisor)):
        return "q: 0 r: " + str(dividend)

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
   
    return "q: " + res + " r: " + str(reminder)

print(divAlg(1, 34, 10))
