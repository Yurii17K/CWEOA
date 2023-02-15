from fast_addition_on_EC import fast_addition
from utils import generate_random_number
from utils_alg import isEqual


def defHelExchange(A, B, p, P:tuple, q):
    x = generate_random_number(1, q)
    Pa = fast_addition(A, p, P, x)
    print("Alice's point: ", Pa)
    y = x
    #ensure that original multipliers are different as time seed might be the same for some bizarre reasons
    while isEqual(x, y):
        y = generate_random_number(1, q)
    Pb = fast_addition(A, p, P, y)
    print("Bob's point: ", Pb)
    Qa = fast_addition(A, p, Pa, y)
    print("Result of Alice multiplying Bob's point by her original multiplier: ", Qa)
    Qb = fast_addition(A, p, Pb, x)
    print("Result of Bob multiplying Alices's point by his original multiplier: ", Qb)
    if isEqual(Qa, Qb):
        print("The secret shared key is: ", Qb)
    else:
        raise Exception("The secret secret is not the same! Developer is an idiot")
    return Qa

# slow
# defHelExchange(51625147243288, 20203625453253, 125565704917787, (44144503758425, 50550630942493), 20)

# to test quickly
# defHelExchange(33, 54, 71, (14, 44), 20)
