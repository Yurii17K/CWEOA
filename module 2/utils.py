import time

def generate_random_number(lower, upper):
  # Seed the random number generator with the current time
  seed = int(time.time())
  
  # Generate a random number in the range [lower, upper]
  return (seed * 9301 + 49297) % 233280 % (upper - lower + 1) + lower

def generate_random_odd_number(k):
  # Generate a random number in the range [2^(k-1), 2^k - 1]
  lower = 1 << (k - 1)
  upper = (1 << k) - 1
  n = generate_random_number(lower, upper)
  
  # Make the number odd by setting the least significant bit to 1
  return n | 1

def mod_pow(a, b, m):
  # Initialize the result to 1
  result = 1
  
  # Calculate a^b mod m using the repeated squaring algorithm
  while b > 0:
    if b % 2 == 1:
      result = (result * a) % m
    a = (a * a) % m
    b //= 2
    
  return result


def is_prime(p):
  # Fermat primality test
  a = generate_random_number(2, p - 2)
  return mod_pow(a, p - 1, p) == 1


def generate_random_prime(k):
  # Generate a random odd number with k bits
  p = generate_random_odd_number(k)
  
  # Use the Fermat primality test to check if p is prime
  while not is_prime(p):
    p = generate_random_odd_number(k)
    
  return p