import random
from utils import generate_random_prime, generate_random_number

def generate_elliptic_curve(k):
  # Generate a random prime number p with k bits
  p = generate_random_prime(k)
  
  # Keep generating (A, B) until 4A^3 + 27B^2 is not 0 (mod p)
  while True:
    A = generate_random_number(0, p - 1)
    B = generate_random_number(0, p - 1)
    if (4 * A ** 3 + 27 * B ** 2) % p != 0:
      break
      
  return (p, A, B)





print(generate_elliptic_curve(10))