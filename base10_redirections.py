# this file is needed to avoid circular dependencies when trying to implement addition of negative numbers,
# as a subtration algorithm is needed but is unavailable because it depends on the addition algorithm
from diff_alg import diffAlgB10
from sum_alg import sumAlgB10
from utils_alg import isEqual

# def sumNeg(num1, num2):
#     raise Exception("Developer has a mistake somewhere, there cant be negative numbers over FF")
#     num1 = str(num1)
#     num2 = str(num2)
#     num1IsNegative = isEqual(num1[0], '-')
#     num2IsNegative = isEqual(num2[0], '-')

#     if not num1IsNegative and not num2IsNegative:
#         return sumAlgB10(num1, num2)

#     if num1IsNegative and num2IsNegative:
#         return int(str('-' + sumAlgB10(num1[1:], num2[1:])))
#     elif (not num1IsNegative and num2IsNegative):
#         return diffAlgB10(num1, num2[1:])
#     else: return diffAlgB10(num2, num1[1:])
    
