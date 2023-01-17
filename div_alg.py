from sum_alg import sumAlgB10, sumAlg
from diff_alg import diffAlg, isBigger
from utils_alg import *

def divAlgB10(dividend, divisor):
    # no idea how and why but for insanely large numbers it happened once, so here's an error
    if isEqual(divisor, 0):
        raise ValueError("CAN NOT DIVIDE BY ZERO")
    if isEqual(str(dividend)[0], '-') or isEqual(str(divisor)[0], '-'):
        raise Exception("Developer has a mistake somewhere, there cant be negative numbers over FF")
        # return divWithNeg(str(dividend), str(divisor))
    return divAlg(dividend, divisor, 10)

# def divAlgImproved(dividend, divisor, base):
#     if (isSmaller(dividend, divisor)):
#         return (0, int(dividend))

#     dividend = list(str(dividend))
#     divisor = str(divisor)
#     reminder = 0
#     res = ""

#     dividendLen = len(dividend)

#     tmpSum = 0

#     while True: # divisors can't be larger than 9, but just to be safe in this crazy world
#         if (isSmaller(tmpSum, dividend)):
#             tmpSum = sumAlg(tmpSum, divisor, base)
#         else:
#             if (isBigger(tmpSum, dividend)): 
#                 multiplications = diffAlg(multiplications, 1, base=10)
#                 tmpSum = diffAlg(tmpSum, divisor, base)
#             res += str(multiplications)
#             reminder = diffAlg(dividend, tmpSum, base)
#             dividend[dividend] = str(reminder)
#             break


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
                        multiplications = diffAlg(multiplications, 1, base=10, prime=None)
                        tmpSum = diffAlg(tmpSum, divisor, base, None)
                    res += str(multiplications)
                    reminder = diffAlg(tmpDividend, tmpSum, base, None)
                    dividend[dividendEndPointer] = str(reminder)
                    dividendStartPointer = dividendEndPointer
                    break
        
        # increase pointer
        dividendEndPointer = sumAlg(dividendEndPointer, 1, base=10)
   
    return (int(res), reminder)
    
# def divWithNeg(dividend, divisor):
#     negative = True

#     dividentIsNegative = isEqual(dividend[0], '-')
#     divisorIsNegative =  isEqual(divisor[0], '-')

#     if dividentIsNegative and not divisorIsNegative:
#         dividend = dividend[1:]
#     elif not dividentIsNegative and divisorIsNegative:
#         divisor = divisor[1:]
#     elif dividentIsNegative and divisorIsNegative:
#         dividend = dividend[1:]
#         divisor = divisor[1:]
#         negative = False

#     multiplications = 0
#     tmpSum = 0
#     while(isSmaller(tmpSum, dividend)):
#         multiplications = sumAlgB10(multiplications, 1)
#         tmpSum = sumAlgB10(tmpSum, divisor)

#     quotient = str(multiplications)
#     reminder = diffAlg(tmpSum, dividend, 10, None)

#     if negative:
#         return (int('-' + quotient), reminder)
#     else: return(int(quotient), reminder)

# print(divAlg(12312312312312, 1231231231, 10))
# print(divAlgB10(-34, 12))
