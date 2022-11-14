from sum_alg import sumAlg
from diff_alg import diffAlg

def multAlg(num1, num2, base):
    longerNum = str(num1)
    shorterNum = str(num2)
    res = ""
    carry = 0

    if (len(longerNum) < len(shorterNum)):
        tmpSwap = longerNum
        longerNum = shorterNum
        shorterNum = tmpSwap
    
    longerNumLen = len(longerNum)
    shorterNumLen = len(shorterNum)

    for lowerRowI in range(shorterNumLen):
        tmpRowMult = ""
        for upperRowI in range(longerNumLen):
            tmpMult = 0

            # perform 'multiplication' by adding the lowerNum upperNum-times to itself
            for y in range(int(longerNum[diffAlg(diffAlg(longerNumLen, upperRowI, base=10), 1, base=10)])):
                tmpMult = sumAlg(tmpMult, shorterNum[diffAlg(diffAlg(shorterNumLen, lowerRowI, base=10), 1, base=10)], base)

            tmpMult = sumAlg(tmpMult, carry, base) # add carry

            baseDivisions = 0
            if (upperRowI != longerNumLen - 1):
                # perform 'division' by base to get the result and a carry
                while (tmpMult >= base):
                    tmpMult = diffAlg(tmpMult, base, base)
                    baseDivisions = sumAlg(baseDivisions, 1, base)
                carry = baseDivisions
            else: carry = 0 # do not divide for last (first in written form) number of the upper row

            tmpRowMult += str(tmpMult)[::-1]

        res = sumAlg(res, int(tmpRowMult[::-1] + ('0' * lowerRowI)), base)

    return res