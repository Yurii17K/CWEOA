from utils import generate_random_prime, generate_random_number, mod_pow
from utils_alg import isEqual
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from mult_alg import multAlgB10
from sum_alg import sumAlgB10

from opposite_of_point_on_EC import mod_inv

def add_points(p, A, B, x1, y1, x2, y2):
  # Check for the point at infinity
  if isEqual(x1, None):
    return (x2, y2)
  if isEqual(x2, None):
    return (x1, y1)
  
  # Calculate the slope of the line
  if isEqual(x1, x2) and isEqual(y1, y2):
    # Calculate the slope of the tangent line
    m = multAlgB10(sumAlgB10(multAlgB10(3, mod_pow(x1, 2, p)), A), mod_inv(multAlgB10(2, y1), p))
  else:
    # Calculate the slope of the line connecting the points
    m = multAlgB10((diffAlgB10(y2, y1)), mod_inv(diffAlgB10(x2, x1), p))
  
  # Calculate the coordinates of the result point
  x3 = divAlgB10(diffAlgB10(diffAlgB10(mod_pow(m, 2, 2), x1), x2), p)[1]
  y3 = divAlgB10(diffAlgB10(multAlgB10(m, (diffAlgB10(x1, x3))), y1), p)[1]
  
  return (x3, y3)


# TESTS
# print(add_points(811, 319, 193, 754, 329 , 761, 324))