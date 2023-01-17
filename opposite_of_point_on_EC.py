from utils import generate_random_prime, generate_random_number, mod_pow
from utils_alg import isEqual
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from mult_alg import multAlgB10

def find_inverse(p, P:tuple):
  # # Calculate the modular inverse of y
  # y_inv = mod_inv(y, p)
  
  # Return the opposite point
  return (divAlgB10(P[0], p)[1], divAlgB10(diffAlgB10(p, P[1], p), p)[1])

# def mod_inv(y, p):
#   # Calculate the extended Euclidean algorithm
#   gcd, x_complement, y_complement = ext_eucl(y, p)
  
#   # Check if y and p are coprime
#   if not isEqual(gcd, 1):
#     raise ValueError("Not coprimes")
  
#   # Calculate the modular inverse of y
#   return divAlgB10(x_complement, p)[1]

# def ext_eucl(y, p):
#   if isEqual(y, 0):
#     return (p, 0, 1)
#   else:
#     gcd, x_complement, y_complement = ext_eucl(divAlgB10(p, y)[1], y)
#     return (gcd, diffAlgB10(y_complement, multAlgB10((p // y), x_complement)), x_complement)


# TESTS
# print(find_opposite(p=643, P=(81, 565)))
# print(find_opposite(p=271, P=(95, 50)))
# print(divAlgB10(diffAlgB10(13, 28), 13))