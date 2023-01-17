import time

from utils_alg import isBigger, isEqual, isSmaller
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from sum_alg import sumAlgB10
from mult_alg import multAlgB10

def div_over_FF(divident, divisor, p):
  return divAlgB10(multAlgB10(divident, mod_pow(divisor, diffAlgB10(p, 2, None), p)), p)[1]
  
def generate_random_number(lower, upper):
  # Seed the random number generator with the current time
  seed = int(time.time())
  
  # Generate a random number in the range [lower, upper]
  return sumAlgB10(
    divAlgB10(
      divAlgB10(
        (sumAlgB10(
          multAlgB10(seed, 9301), 
          49297)), 
        233280)[1], 
      sumAlgB10(
        diffAlgB10(upper, lower, None),
         1))[1], 
    lower)

def generate_random_odd_number(k):
  # Generate a random number in the range [2^(k-1), 2^k - 1]
  lower = 1 << (diffAlgB10(k, 1, None))
  upper = diffAlgB10((1 << k), 1, None)
  n = generate_random_number(lower, upper)
  
  # Make the number odd by setting the least significant bit to 1
  return n | 1

def generate_random_odd_number_in(lower, upper):
  n = generate_random_number(lower, upper)
  
  # Make the number odd by setting the least significant bit to 1
  return n | 1

def mod_pow(a, b, p):
  # Initialize the result to 1
  result = 1
  
  # Calculate a^b mod m using the repeated squaring algorithm
  while isBigger(b, 0):
    if isEqual(divAlgB10(b, 2)[1], 1):
      result = divAlgB10(multAlgB10(result, a), p)[1]
    a = divAlgB10(multAlgB10(a, a), p)[1]
    b = divAlgB10(b, 2)[0]
    
  return result

def sqrt_int_part(n, p):
  # tonneli shanks alg
  if isEqual(p, 2):
      return n & 1
  if not isEqual(legendre_symbol(n, p), 1):
      return None
  if isEqual(divAlgB10(p, 4)[1], 3):
      return mod_pow(n, sumAlgB10(p, 1) // 4, p)
  s = 0
  q = diffAlgB10(p, 1, p)
  while isEqual(divAlgB10(q, 2)[1], 0):
      q //= 2
      s = sumAlgB10(s, 1)
  if isEqual(s, 1):
      return mod_pow(n, sumAlgB10(p, 1) // 4, p)
  for z in range(2, p):
      if isEqual(diffAlgB10(p, 1, p), legendre_symbol(z, p)):
          break
  c = mod_pow(z, q, p)
  r = mod_pow(n, sumAlgB10(q, 1) // 2, p)
  t = mod_pow(n, q, p)
  m = s
  t2 = 0
  while not isEqual(divAlgB10(diffAlgB10(t, 1, p), p)[1], 0):
      t2 = divAlgB10(multAlgB10(t, t), p)[1]
      for i in range(1, m):
          if isEqual(divAlgB10(diffAlgB10(t2, 1, p), p)[1], 0):
              break
          t2 = divAlgB10(multAlgB10(t2, t2), p)[1]
      b = mod_pow(c, 1 << diffAlgB10(diffAlgB10(m, i, p), 1, p), p)
      r = divAlgB10(multAlgB10(r, b), p)[1]
      c = divAlgB10(multAlgB10(b, b), p)[1]
      t = divAlgB10(multAlgB10(t, c), p)[1]
      m = i
  return r

def legendre_symbol(a, p):
    return mod_pow(a, diffAlgB10(p, 1, p) // 2, p)

def is_prime(p):
  # Fermat primality test
  a = generate_random_number(2, diffAlgB10(p, 2, p))
  return isEqual(mod_pow(a, diffAlgB10(p, 1, p), p), 1)


def generate_random_prime(k):
  # Generate a random odd number with k bits
  p = generate_random_odd_number(k)
  
  # Use the Fermat primality test to check if p is prime
  while not is_prime(p):
    p = generate_random_odd_number(k)
    print("Number " + str(p) + " not a prime. Searching for a prime with " + str(k) + " bits...")
    
  return p


# Generate a random prime number p with k bits untill it satisfies p % 4 == 3
def generate_random_prime_3_mod_4(k):
   while not isEqual(divAlgB10(p, 4)[1], 3):
    print("Generating prime...")
    p = generate_random_prime(k)


def generate_random_prime_in(lower, upper):
  # Generate a random odd number with k bits
  p = generate_random_odd_number_in(lower, upper)
  
  # Use the Fermat primality test to check if p is prime
  while not is_prime(p):
    p = generate_random_odd_number_in(lower, upper)
    
  return p

# TEST
# print(sqrt_int_part(2, 7))
# print(mod_pow(3, 2, 7))