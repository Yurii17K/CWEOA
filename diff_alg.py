from sum_alg import sumAlg
from utils_alg import *

def diffAlg(num1, num2, base):
    longerNum = list(str(num1))
    shorterNum = list(str(num2))
    res = ""
    swapped = False

    if (isSmaller(longerNum, shorterNum)):
        tmpSwap = longerNum
        longerNum = shorterNum
        shorterNum = tmpSwap
        swapped = True

    longerNumLen = len(longerNum)
    shorterNumLen = len(shorterNum)

    for x in range(shorterNumLen):
        upperNum = int(longerNum[longerNumLen - 1 - x]) # could use a diffLT to subtract '1', but x might be to large
        lowerNum = int(shorterNum[shorterNumLen - 1 - x])

        # 'borrow' from the next column
        if (upperNum < lowerNum):
            upperNum = sumAlg(upperNum, base, base=10)

            # look for a column with a non-zero number
            for y in range(longerNumLen - x - 1):
                longerNum[longerNumLen - 2 - y - x] = diffLT(int(longerNum[longerNumLen - 2 - y - x]), 1)
                if (int(longerNum[longerNumLen - 2 - y - x]) > -1):
                    break
                
        # perform basic subtraction
        tmpDiff = diffLT(upperNum, lowerNum)

        # perform 'division' by base to get the result (can't explain, been coding for 5h -_-)
        while (isBiggerOrEqual(tmpDiff, base)):
            tmpDiff = diffLT(tmpDiff, base)
        res += str(tmpDiff)

    # just bring down the elements from the upper raw
    for x in range(shorterNumLen, longerNumLen):
        res += str(longerNum[longerNumLen - 1 - x])

    # put '-' if the first number was smaller
    if (swapped):
        return int('-' + res[::-1])
    else: return int(res[::-1])

# print(diffAlg(1100, 101, 2))