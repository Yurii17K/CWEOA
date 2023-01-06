from utils import generate_random_prime, generate_random_number, mod_pow
from utils_alg import isEqual
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from sum_alg import sumAlgB10
from mult_alg import multAlgB10

def gen_prime_find_point(A, B):
  # 100 bit prime
  p = generate_random_prime(10)

  # Generate a random prime number p with k bits untill it satisfies p % 4 == 3
  while not isEqual(divAlgB10(p, 4)[1], 3):
    print("Generating prime...")
    p = generate_random_prime(10)

  return find_random_point(A, B, p)



def find_random_point(A, B, p):
  # Generate a random point (x, y) on the elliptic curve
  x = generate_random_number(0, diffAlgB10(p, 1))
  y = divAlgB10(sumAlgB10(sumAlgB10(mod_pow(x, 3, p), multAlgB10(A, x)), B), p)[1]
  
  # Check if (x, y) is on the curve
  if isEqual(mod_pow(y, 2, p), y):
    return (A, B, p, x, '+-' + str(y))
  else:
    print("Not suitable point, trying again")
    # If (x, y) is not on the curve, try again
    return find_random_point(A, B, p)


# TEST
print(gen_prime_find_point(4, 5))
