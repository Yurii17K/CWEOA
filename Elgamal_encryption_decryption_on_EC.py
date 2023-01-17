from utils import generate_random_odd_number_in
from div_alg import divAlgB10
from diff_alg import diffAlgB10
from public_private_keys import find_order
from fast_addition_on_EC import fast_addition
from message_encoding_decoding import encode_message
from add_points_EC import add_points
from opposite_of_point_on_EC import find_inverse
from utils import div_over_FF
from utils_alg import isEqual 
from sum_alg import sumAlgB10

def elg_en_on_ec(A, B, p, Q:tuple, M):
    q = find_order(A, Q, p)
    x = generate_random_odd_number_in(1, diffAlgB10(q, 1, p))
    key = generate_random_odd_number_in(1, diffAlgB10(q, 1, p))
    P = fast_addition(A, p, Q, x)
    Pm, kappa = encode_message(A, B, p, M)
    C1 = fast_addition(A, p, Q, key)
    C2 = add_points(A, p, Pm, fast_addition(A, p, P, key))
    return C1, C2, kappa, x

def elg_decr_on_ec(A, p, kappa, x, C1:tuple, C2:tuple):
    Pm = add_points(A, p, C2, find_inverse(p, fast_addition(A, p, C1, x)))
    M = divAlgB10(Pm[0], kappa)[0]
    return M

def testCase(A, B, p, Q:tuple,  M):
    C1, C2, kappa, x = elg_en_on_ec(A, B, p, Q, M)
    decr_M = elg_decr_on_ec(A, p, kappa, x, C1, C2)
    return decr_M

# TEST
# print(testCase(319, 193, 811, (754, 329), 17)) # -> for quicker testing replace Q's (q in the top func) order with a precalculated 625


# Either sth is broken or this baby giant step doesnt work, 
# because my find_order finds and order slowly while this doesnt at all
def point_order_EC(A, p, P):
    pStr = str(p)
    pStr = pStr[:sumAlgB10(divAlgB10(len(pStr), 2)[0], 1)]
    m = int(pStr)
    baby_steps = {}
    baby_step = P
    for i in range(m):
        baby_steps[i] = baby_step
        baby_step = add_points(A, p, baby_step, P)
    inv = find_inverse(p, fast_addition(A, p, find_inverse(p, P), m))
    giant_step = (0, 0)
    for j in range(m):
        if isEqual(giant_step[0], baby_steps[j][0]) and isEqual(giant_step[1], baby_steps[j][1]):
            return j
        giant_step = add_points(A, p, giant_step, inv)
    return None

# TEST
# print(point_order_EC(319, 811, (754, 329)))
