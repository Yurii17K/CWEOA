from sum_alg import sumAlg
from diff_alg import diffAlg, isBigger
from utils_alg import *

def divAlg(dividend, divisor, base):
    dividend = list(str(dividend))
    divisor = list(str(divisor))
    reminder = 0
    res = ""

    dividendLen = len(dividend)
    divisorLen = len(divisor)

    if (not isBigger(dividendLen, divisorLen)):
        return "q: " + dividend + " r: 0"

    if (isEqual(dividendLen, divisorLen) and not isBigger(dividend, divisor)):
            return "q: " + dividend + " r: 0"

    for dividendI in range(dividendLen):
        if(not isBigger(dividendLen[:dividendI], divisor)):
            reminder = int(dividendLen[:dividendI])
            continue
        else: 
            tmpDivident = dividendLen[:dividendI + 1]
            reminder = 0
            tmpSum = 0
            for multiplications in range(20): # divisors can't be larger than 9, but just to be safe in this crazy world
                if(not isBigger(tmpSum, tmpDivident)):
                    tmpSum = sumAlg(tmpSum, divisor, base)
                else: 
                    res += str(multiplications - 1)
                    reminder = diffAlg(tmpDivident, tmpSum - divisor, base)
                    dividend[dividendI] = reminder
                    dividendI = diffAlg(dividendI, 1, base=10)
                    break
   
    return "q: " + res + "r: " + reminder

print(divAlg(100, 10, 10))
