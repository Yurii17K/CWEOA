from utils import generate_random_prime, generate_random_number, mod_pow
from utils_alg import isEqual
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from sum_alg import sumAlgB10
from mult_alg import multAlgB10

def generate_elliptic_curve(k):
  # Generate a random prime number p with k bits
  p = generate_random_prime(k)

  # Generate a random prime number p with k bits untill it satisfies p % 4 == 3
  while not isEqual(divAlgB10(p, 4)[1], 3):
    p = generate_random_prime(k)
  
  # Keep generating (A, B) until 4A^3 + 27B^2 is not 0 (mod p)
  while True:
    A = generate_random_number(0, diffAlgB10(p, 1))
    B = generate_random_number(0, diffAlgB10(p, 1))
    if not isEqual(divAlgB10(sumAlgB10(mod_pow(multAlgB10(4, A), 3, p), mod_pow(multAlgB10(27, B), 2, p)), p)[1], 0):
      break
      
  return (p, A, B)


# TEST
print(generate_elliptic_curve(10))