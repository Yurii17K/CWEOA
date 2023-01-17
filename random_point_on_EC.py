from utils import generate_random_number, mod_pow, sqrt_int_part
from utils_alg import isEqual
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from sum_alg import sumAlgB10
from mult_alg import multAlgB10

def find_random_point(A, B, p):
  # Generate a random point (x, y) on the elliptic curve
  x = generate_random_number(0, diffAlgB10(p, 1, p))
  yPow2 = divAlgB10(sumAlgB10(sumAlgB10(mod_pow(x, 3, p), multAlgB10(A, x)), B), p)[1]
  
  # Check if (x, y) is on the curve
  if is_quadratic_residue(yPow2, p):
    print("Found random point X: " + str(x) + " Y^2: " + str(yPow2) + " on the EC")
    return (x, sqrt_int_part(yPow2, p))
  else:
    print("Random point X: " + str(x) + " Y^2: " + str(yPow2) + " not on the EC, searching again...")
    # If (x, y) is not on the curve, try again
    return find_random_point(A, B, p)

def find_point__with_x_given(A, B, p, x):
  yPow2 = divAlgB10(sumAlgB10(sumAlgB10(mod_pow(x, 3, p), multAlgB10(A, x)), B), p)[1]
  
  # Check if (x, y) is on the curve
  if is_quadratic_residue(yPow2, p):
    print("Found point X: " + str(x) + " Y^2: " + str(yPow2) + " on the EC")
    return (x, sqrt_int_part(yPow2, p)) 
  else:
    return None, None
    # raise Exception("\n\nPoint with fixed X: " + str(x) + """ does not exist on EC denoted 
    # by current A and B, please RUN THE FUNCTION AGAIN for better luck :)
    # \n Don't worry if happens a few times""")

def is_quadratic_residue(a, p):
    legendre_symbol = mod_pow(a, diffAlgB10(p, 1, p) // 2, p)
    return isEqual(legendre_symbol, 1)

# TEST
# print(find_random_point(4, 5, 7))
