from utils import generate_random_number
from div_alg import divAlgB10
from mult_alg import multAlgB10
from sum_alg import sumAlgB10
from random_point_on_EC import find_point__with_x_given

def encode_message(A:int, B:int, p:int, M:int):
    kappa = generate_random_number(1, divAlgB10(p, M)[0])
    j = generate_random_number(1, kappa)
    x = divAlgB10(sumAlgB10(multAlgB10(kappa, M), j), p)[1]
    # This part throws an exception if there is no point with above random X as an x-coordinate
    # Just run the algorithm again for better luck :)
    P = None, None
    while(P[0] is None):
        j = generate_random_number(1, kappa)
        x = divAlgB10(sumAlgB10(multAlgB10(kappa, M), j), p)[1]
        P = find_point__with_x_given(A, B, p, x)
        if (P[0] is None):
            print("""Point with a fixed X: """ + str(x) + """ obtained from random 'kappa' and 'j' does not exist on EC denoted 
                         by current A and B, trying with another X""")
        else : break
    # if Px / kappa equals to M then hurray
    return P, kappa

# TEST
# print(encode_message(70471581, 353525814, 370870547, 811999))