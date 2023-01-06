from utils import generate_random_prime, generate_random_number, mod_pow
from utils_alg import isEqual
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from sum_alg import sumAlgB10
from mult_alg import multAlgB10

def is_on_EC(A, B, x, y, p):
    # Check if (x, y) is on the curve
    if isEqual(mod_pow(y, 2, p), y):
        return True
    else: return False

# TEST
# should pass
print(is_on_EC(4, 5, 18, 0, 19))
print(is_on_EC(A=9, B=20, x=23, y=10, p=12))
# should not pass
print(is_on_EC(255710314389904331078423537081, 99813867828486316864100780197, 741410741199617876054224771219, 
619709014043226523215974051800, 502193949210502663079510993753))
