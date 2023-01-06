import time

from utils_alg import isBigger, isEqual
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from sum_alg import sumAlgB10
from mult_alg import multAlgB10

def generate_random_number(lower, upper):
  # Seed the random number generator with the current time
  seed = int(time.time())
  
  # Generate a random number in the range [lower, upper]
  return sumAlgB10(divAlgB10(divAlgB10((sumAlgB10(multAlgB10(seed, 9301), 49297)), 233280)[1], (sumAlgB10(diffAlgB10(upper, lower), 1)))[1], lower)

def generate_random_odd_number(k):
  # Generate a random number in the range [2^(k-1), 2^k - 1]
  lower = 1 << (diffAlgB10(k, 1))
  upper = diffAlgB10((1 << k), 1)
  n = generate_random_number(lower, upper)
  
  # Make the number odd by setting the least significant bit to 1
  return n | 1

def generate_random_odd_number_in(lower, upper):
  n = generate_random_number(lower, upper)
  
  # Make the number odd by setting the least significant bit to 1
  return n | 1

def mod_pow(a, b, m):
  # Initialize the result to 1
  result = 1
  
  # Calculate a^b mod m using the repeated squaring algorithm
  while isBigger(b, 0):
    if isEqual(divAlgB10(b, 2)[1], 1):
      result = divAlgB10(multAlgB10(result, a), m)[1]
    a = divAlgB10(multAlgB10(a, a), m)[1]
    b //= 2
    
  return result


def is_prime(p):
  # Fermat primality test
  a = generate_random_number(2, diffAlgB10(p, 2))
  return isEqual(mod_pow(a, diffAlgB10(p, 1), p), 1)


def generate_random_prime(k):
  # Generate a random odd number with k bits
  p = generate_random_odd_number(k)
  
  # Use the Fermat primality test to check if p is prime
  while not is_prime(p):
    p = generate_random_odd_number(k)
    
  return p


def generate_random_prime_in(lower, upper):
  # Generate a random odd number with k bits
  p = generate_random_odd_number_in(lower, upper)
  
  # Use the Fermat primality test to check if p is prime
  while not is_prime(p):
    p = generate_random_odd_number_in(lower, upper)
    
  return p