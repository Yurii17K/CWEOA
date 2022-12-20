import random
from random_EC import generate_random_prime

def find_random_point(A, B):
  p = generate_random_prime(10)

  # Generate a random point (x, y) on the elliptic curve
  x = random.randint(0, p - 1)
  y = (x ** 3 + A * x + B) % p
  
  # Check if (x, y) is on the curve
  if (y ** 2) % p == (x ** 3 + A * x + B) % p:
    return (A, B, p, x, +-y)
  else:
    # If (x, y) is not on the curve, try again
    return find_random_point(A, B)

print(find_random_point(4, 5))