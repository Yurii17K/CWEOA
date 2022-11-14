from utils_alg import *

def sumAlg(num1, num2, base):
    # base = int(input("Input future numbers' base (up to 10 inclusive): \n"))
    # longerNum = input("Input the 1st num: \n")
    # shorterNum = input("Input the 2nd num: \n")

    longerNum = list(str(num1))
    shorterNum = list(str(num2))
    res = ""
    reminder = 0

    if (len(longerNum) < len(shorterNum)):
        tmpSwap = longerNum
        longerNum = shorterNum
        shorterNum = tmpSwap

    for x in range(len(shorterNum)):
        if (((len(shorterNum) - 2 - x) >= 0) and shorterNum[len(shorterNum) - 2 - x] == '-'):
            shorterNum.pop(len(shorterNum) - 2 - x)
            shorterNum[len(shorterNum) - 1 - x] = '-' + shorterNum[len(shorterNum) - 1 - x]
        tmpSum = sumLT(sumLT(int(longerNum[len(longerNum) - 1 - x]), int(shorterNum[len(shorterNum) - 1 - x])), reminder)
        if (tmpSum >= base):
            reminder = 1
            res += str(diffLT(tmpSum, base))
        else: 
            reminder = 0
            res += str(tmpSum)

    for x in range(len(shorterNum), len(longerNum)):
        if (((len(longerNum) - 2 - x) >= 0) and longerNum[len(longerNum) - 2 - x] == '-'):
            longerNum.pop(len(longerNum) - 2 - x)
            longerNum[len(longerNum) - 1 - x] = '-' + longerNum[len(longerNum) - 1 - x]
        tmpSum = sumLT(int(longerNum[len(longerNum) - 1 - x]), reminder)
        if (tmpSum >= base):
            reminder = 1
            res += str(diffLT(tmpSum, base))
        else: 
            reminder = 0
            res += str(tmpSum)

    if (reminder != 0):
        res += str(reminder)

    return int(res[::-1])

# print(sumAlg(-10, -10, 10))