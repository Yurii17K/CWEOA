from utils_alg import *

def sumAlg(num1, num2, base):
    # base = int(input("Input future numbers' base (up to 10 inclusive): \n"))
    # longerNum = input("Input the 1st num: \n")
    # shorterNum = input("Input the 2nd num: \n")

    longerNum = list(str(num1))
    shorterNum = list(str(num2))
    res = ""
    reminder = 0
    minusesFoundInLongerNumber = 0

    if (isSmaller(longerNum, shorterNum)):
        tmpSwap = longerNum
        longerNum = shorterNum
        shorterNum = tmpSwap

    longerNumLen = len(longerNum)
    shorterNumLen = len(shorterNum)

    longerNumI = 1
    shorterNumI = 1
    while (isSmaller(shorterNumI, shorterNumLen + 1)):

        shiftDueToUpperMinus = 0
        shiftDueToLowerMinus = 0

        # negative numbers handling in the uppper row
        if (isBiggerOrEqual(longerNumLen - 1 - longerNumI, 0) and isEqual(longerNum[longerNumLen - 1 - longerNumI], '-')):
            longerNum[longerNumLen - longerNumI] = '-' + longerNum[longerNumLen - longerNumI]
            longerNumI += 1
            minusesFoundInLongerNumber += 1
            shiftDueToUpperMinus += 1
        
        if (isBiggerOrEqual(shorterNumLen - 1 - shorterNumI, 0) and isEqual(shorterNum[shorterNumLen - 1 - shorterNumI], '-')):
            shorterNum[shorterNumLen - shorterNumI] = '-' + shorterNum[shorterNumLen - shorterNumI]
            shorterNumI += 1
            shiftDueToLowerMinus += 1

        tmpSum = sumLT(sumLT(
                            int(longerNum[longerNumLen - longerNumI - shiftDueToUpperMinus]),
                            int(shorterNum[shorterNumLen - shorterNumI - shiftDueToLowerMinus])),
                    reminder)
                
        # rounding to a base
        if (isBiggerOrEqual(tmpSum, base)):
            reminder = 1
            res += str(diffLT(tmpSum, base))
        else: 
            reminder = 0
            res += str(tmpSum)

        longerNumI += 1
        shorterNumI += 1

    longerNumI = shorterNumLen + minusesFoundInLongerNumber + 1
    while (isSmaller(longerNumI, longerNumLen + 1)):

        # negative numbers handling
        if (isBiggerOrEqual(longerNumLen - 1 - longerNumI, 0) and isEqual(longerNum[longerNumLen - 1 - longerNumI], '-')):
            longerNum[longerNumLen - longerNumI] = '-' + longerNum[longerNumLen - longerNumI]
            longerNumI += 1
            tmpSum = sumLT(int(longerNum[longerNumLen - longerNumI - 1]), reminder)
        else: 
            tmpSum = sumLT(int(longerNum[longerNumLen - longerNumI]), reminder)

        # rounding to a base
        if (isBiggerOrEqual(tmpSum, base)):
            reminder = 1
            res += str(diffLT(tmpSum, base))
        else: 
            reminder = 0
            res += str(tmpSum)

        longerNumI += 1

    if (not isEqual(reminder, 0)):
        res += str(reminder)

    return int(res[::-1])

print(sumAlg(-11, 1011, 2))