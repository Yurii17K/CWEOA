from sum_alg import sumAlg
from utils_alg import *

def diffAlg(num1, num2, base):
    longerNum = list(str(num1))
    shorterNum = list(str(num2))
    res = ""
    swapped = False
    lenderExists = True

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
        if (isSmaller(upperNum, lowerNum)):

            # stop if the left-most element of the upper number is smaller than the corresponding element of a lower element due to constant 'borrowwing'
            if (isEqual(x + 1, longerNumLen)):
                break

            # 'borrow' a base
            upperNum = sumAlg(upperNum, base, base=10)

            # look for a column with a non-zero number
            lenderExists = False
            for y in range(longerNumLen - x - 1):
                longerNum[longerNumLen - 2 - y - x] = diffLTNoNegatives(int(longerNum[longerNumLen - 2 - y - x]), 1)
                currentNum = int(longerNum[longerNumLen - 2 - y - x])
                if (not isEqual(currentNum, 9) and isBiggerOrEqual(currentNum, 0)):
                    lenderExists = True
                    break
        
        # imagine 100 - 99, already on a second iteration there won't be any elements to borrow from
        if (not lenderExists): break

        # perform basic subtraction
        tmpDiff = diffLT(upperNum, lowerNum)

        # perform 'division' by base to get the result (can't explain, been coding for 5h -_-)
        while (isBiggerOrEqual(tmpDiff, base)):
            tmpDiff = diffLT(tmpDiff, base)
        res += str(tmpDiff)

    # just bring down the elements from the upper raw
    if (lenderExists):
        for x in range(shorterNumLen, longerNumLen):
            res += str(longerNum[longerNumLen - 1 - x])

    # put '-' if the first number was smaller
    if (swapped):
        return int('-' + res[::-1])
    else: return int(res[::-1])

print(diffAlg(-1, 72, 10))