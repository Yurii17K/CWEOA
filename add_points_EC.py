from utils import mod_pow
from utils_alg import isEqual
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from mult_alg import multAlgB10
from sum_alg import sumAlgB10

from opposite_of_point_on_EC import mod_inv

def add_points(A, p, P1, P2):
    if P1[0] is None:
        return P2
    if P2[0] is None:
        return P1
    # If P1 and P2 have different x-coordinates, compute the slope of the line through P1 and P2
    if not isEqual(P1[0], P2[0]):
        # Compute the slope of the line through P1 and P2
        alpha = divAlgB10(diffAlgB10(P2[1], P1[1]), diffAlgB10(P2[0], P1[0]))[1]

        # Compute the x-coordinate of the result R
        x = divAlgB10(diffAlgB10(diffAlgB10(mod_pow(alpha, 2, p), P1[0]), P2[0]), p)[1]
        # Compute the y-coordinate of the result R
        y = divAlgB10(diffAlgB10(multAlgB10(alpha, diffAlgB10(P1[0], x)), P1[1]), p)[1]

        return (x, y)
    # If P1 and P2 have the same x-coordinate, but different y-coordinates, return the point at infinity
    elif not isEqual(P1[1], P2[1]):
        return (None, None)
    # If P1 and P2 are the same point, return the result of doubling P1
    else:
        alpha = divAlgB10(divAlgB10(
                    divAlgB10(sumAlgB10(multAlgB10(3, mod_pow(P1[0], 2, p)), A), p)[1],  # nominator modulo p
                    divAlgB10(multAlgB10(2, P1[1]), p)[1] # denominator modulo p
                )[0], # dividing nominator by denominator
            p)[1] # modulo of the above division

        x = divAlgB10(diffAlgB10(mod_pow(alpha, 2, p), multAlgB10(2, P1[0])), p)[1]
        y = divAlgB10(diffAlgB10(multAlgB10(alpha, diffAlgB10(P1[0], x)), P1[1]), p)[1]

        return (x, y)


# TESTS
# print(add_points(33, 71, (41, 61), (41, 61)))