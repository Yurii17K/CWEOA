from fast_addition_on_EC import fast_addition, add_points
from random_point_on_EC import find_random_point
from utils_alg import *
from utils import generate_random_number
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from random_EC import generate_elliptic_curve

def pub_pr_keys(k):
    p, A, B = generate_elliptic_curve(k)
    Q, order = random_element_of_order_k_div_4(A, B, p, k)
    x = generate_random_number(1, diffAlgB10(order, 1))
    P = fast_addition(A, p, Q, x)
    return (A, B, p, Q, P, x)

def find_order(A, Q, p):
    R = Q

    for x in range(2, p):
        R = add_points(A, p, R, Q)
        if (R[0] is None and R[1] is None) or (isEqual(R[0], 0) and isEqual(R[1], 0)):
            print("Order of a point " + str(Q) + " : " + str(x))
            return x
        print("Calculating order of a point " + str(Q) + "...")

    return 0

def random_element_of_order_k_div_4(A, B, p, k):
    order = 0
    Q = (None, None)

    while True:
        Q = find_random_point(A, B, p)
        order = find_order(A, Q, p)

        # if order of a point is infinite continue
        if isEqual(order, 0):
            print("Order of a point " + str(Q) + " is infinite, trying another point...")
            continue

        if isSmaller(order, diffAlgB10((1 << divAlgB10(k, 4)[0]), 1)):
            print("Searching for an EC element with order at least k/4 bits...")
        else: return (Q, order)

# TESTS
# for x in range(1, 30):
print(pub_pr_keys(5))