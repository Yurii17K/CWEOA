from sum_alg import sumAlg
from utils_alg import *

def diffAlg(num1, num2, base):
    longerNum = list(str(num1))
    shorterNum = list(str(num2))
    res = ""
    # carry = 0
    swapped = False

    if (isSmaller(longerNum, shorterNum)):
        tmpSwap = longerNum
        longerNum = shorterNum
        shorterNum = tmpSwap
        swapped = True

    longerNumLen = len(longerNum)
    shorterNumLen = len(shorterNum)

    for x in range(shorterNumLen):
        upperNum = int(longerNum[longerNumLen - 1 - x])
        lowerNum = int(shorterNum[shorterNumLen - 1 - x])

        if (upperNum < lowerNum):
            # carry = sumAlg(carry, 1, base)
            upperNum = sumAlg(upperNum, base, base)
            for y in range(longerNumLen - x - 1):
                longerNum[longerNumLen - 2 - y - x] = diffLT(int(longerNum[longerNumLen - 2 - y - x]), 1)
                if (int(longerNum[longerNumLen - 2 - y - x]) > -1):
                    break
                
        tmpDiff = diffLT(upperNum, lowerNum)
        while (tmpDiff >= base):
            tmpDiff = diffLT(tmpDiff, base)
        res += str(tmpDiff)

    for x in range(shorterNumLen, longerNumLen):
        res += str(longerNum[longerNumLen - 1 - x])

    if (swapped):
        return int('-' + res[::-1])
    else: return int(res[::-1])

# print(diffAlg(1100, 101, 2))