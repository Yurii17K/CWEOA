import time

from diff_alg import diffAlgB10
from div_alg import divAlgB10
from mult_alg import multAlgB10
from sum_alg import sumAlgB10
from utils_alg import isBigger, isEqual, isSmaller


def div_over_FF(divident, divisor, p):
    return divAlgB10(
        multAlgB10(
            divident,
            mod_pow(divisor, diffAlgB10(p, 2, None),
                    p)),
        p)[1]


def generate_random_number(lower, upper):
    # Seed the random number generator with the current time
    seed = int(time.time())

    # Generate a random number in the range [lower, upper]
    return sumAlgB10(
        divAlgB10(
            divAlgB10(
                (sumAlgB10(
                    multAlgB10(seed, 9301),
                    49297)),
                233280)[1],
            sumAlgB10(
                diffAlgB10(upper, lower, None),
                1))[1],
        lower)


def generate_random_odd_number(k):
    # Generate a random number in the range [2^(k-1), 2^k - 1]
    lower = 1 << (diffAlgB10(k, 1, None))
    upper = diffAlgB10((1 << k), 1, None)
    n = generate_random_number(lower, upper)

    # Make the number odd by setting the least significant bit to 1
    return n | 1


def generate_random_odd_number_in(lower, upper):
    n = generate_random_number(lower, upper)

    # Make the number odd by setting the least significant bit to 1
    return n | 1


def mod_pow(base, exponent, p):
    # Initialize the result to 1
    result = 1

    # Calculate a^b mod m using the repeated squaring algorithm
    while isBigger(exponent, 0):
        if isEqual(divAlgB10(exponent, 2)[1], 1):
            result = divAlgB10(multAlgB10(result, base), p)[1]
        base = divAlgB10(multAlgB10(base, base), p)[1]
        exponent = exponent // 2

    return result


def sqrt_int_part(n, p):
    # tonneli shanks alg
    if isEqual(p, 2):
        return n & 1
    if not isEqual(legendre_symbol(n, p), 1):
        return None
    if isEqual(divAlgB10(p, 4)[1], 3):
        return mod_pow(n, sumAlgB10(p, 1) // 4, p)
    s = 0
    q = diffAlgB10(p, 1, p)
    while isEqual(divAlgB10(q, 2)[1], 0):
        q //= 2
        s = sumAlgB10(s, 1)
    if isEqual(s, 1):
        return mod_pow(n, sumAlgB10(p, 1) // 4, p)
    for z in range(2, p):
        if isEqual(diffAlgB10(p, 1, p), legendre_symbol(z, p)):
            break
    c = mod_pow(z, q, p)
    r = mod_pow(n, sumAlgB10(q, 1) // 2, p)
    t = mod_pow(n, q, p)
    m = s
    t2 = 0
    while not isEqual(divAlgB10(diffAlgB10(t, 1, p), p)[1], 0):
        t2 = divAlgB10(multAlgB10(t, t), p)[1]
        for i in range(1, m):
            if isEqual(divAlgB10(diffAlgB10(t2, 1, p), p)[1], 0):
                break
            t2 = divAlgB10(multAlgB10(t2, t2), p)[1]
        b = mod_pow(c, 1 << diffAlgB10(diffAlgB10(m, i, p), 1, p), p)
        r = divAlgB10(multAlgB10(r, b), p)[1]
        c = divAlgB10(multAlgB10(b, b), p)[1]
        t = divAlgB10(multAlgB10(t, c), p)[1]
        m = i
    return r


def legendre_symbol(a, p):
    return mod_pow(a, diffAlgB10(p, 1, p) // 2, p)


def is_prime(p):
    # Fermat primality test
    a = generate_random_number(2, diffAlgB10(p, 2, p))
    return isEqual(mod_pow(a, diffAlgB10(p, 1, p), p), 1)


def generate_random_prime(k):
    # Generate a random odd number with k bits
    p = generate_random_odd_number(k)

    # Use the Fermat primality test to check if p is prime
    while not is_prime(p):
        p = generate_random_odd_number(k)
        print("Number " + str(p) + " not a prime. Searching for a prime with " + str(k) + " bits...")

    return p


# Generate a random prime number p with k bits untill it satisfies p % 4 == 3
def generate_random_prime_3_mod_4(k):
    while not isEqual(divAlgB10(p, 4)[1], 3):
        print("Generating prime...")
        p = generate_random_prime(k)


def generate_random_prime_in(lower, upper):
    # Generate a random odd number with k bits
    p = generate_random_odd_number_in(lower, upper)

    # Use the Fermat primality test to check if p is prime
    while not is_prime(p):
        p = generate_random_odd_number_in(lower, upper)

    return p


# ik a bit wrong with those descriptions, but it does the job
def asciiTable():
    return {
        0: "null", 1: "SOH (start of heading)", 2: "STX (start of text)",
        3: "ETX (end of text)", 4: "EOT (end of transmission)", 5: "ENQ (enquiry)",
        6: "ACK (acknowledge)", 7: "BEL (bell)", 8: "BS (backspace)", 9: "\t",
        10: "\n", 11: "VT (vertical tab)", 12: "FF (form feed)", 13: "\r",
        14: "SO (shift out)", 15: "SI (shift in)", 16: "DLE (data link escape)", 17: "DC1 (device control 1)",
        18: "DC2 (device control 2)", 19: "DC3 (device control 3)", 20: "DC4 (device control 4)",
        21: "NAK (negative acknowledge)",
        22: "SYN (synchronous idle)", 23: "ETB (end of trans. block)", 24: "CAN (cancel)", 25: "EM (end of medium)",
        26: "SUB (substitute)", 27: "ESC (escape)", 28: "FS (file separator)", 29: "GS (group separator)",
        30: "RS (record separator)", 31: "US (unit separator)", 32: " ", 33: "!", 34: "\"", 35: "#", 36: "$",
        37: "%", 38: "&", 39: "'", 40: "(", 41: ")", 42: "*", 43: "+", 44: ",", 45: "-", 46: ".", 47: "/",
        48: "0", 49: "1", 50: "2", 51: "3", 52: "4", 53: "5", 54: "6", 55: "7", 56: "8", 57: "9",
        58: ":", 59: ";", 60: "<", 61: "=", 62: ">", 63: "?", 64: "@", 65: "A", 66: "B", 67: "C",
        68: "D", 69: "E", 70: "F", 71: "G", 72: "H", 73: "I", 74: "J", 75: "K", 76: "L", 77: "M",
        78: "N", 79: "O", 80: "P", 81: "Q", 82: "R", 83: "S", 84: "T", 85: "U", 86: "V", 87: "W",
        88: "X", 89: "Y", 90: "Z", 91: "[", 92: "\\", 93: "]", 94: "^", 95: "_", 96: "`", 97: "a",
        98: "b", 99: "c", 100: "d", 101: "e", 102: "f", 103: "g", 104: "h", 105: "i", 106: "j", 107: "k",
        108: "l", 109: "m", 110: "n", 111: "o", 112: "p", 113: "q", 114: "r", 115: "s", 116: "t", 117: "u",
        118: "v", 119: "w", 120: "x", 121: "y", 122: "z", 123: "{", 124: "|", 125: "}", 126: "~", 127: "DEL (delete)"
    }


def toAsciiToBin(B: str):
    binaryEncoded = ""

    # omit Chat GPT formatting
    B = ''.join(char for char in B if ord(char) < 128)

    charAscii = {value: str(key) for key, value in asciiTable().items()}
    for x in B:
        toAsciiToBin = toBin(charAscii[x])
        binaryEncoded += str(len(toAsciiToBin)) + toAsciiToBin
    return binaryEncoded


def fromBinToAsciiToPlain(binaryEncoded: str):
    table = {str(key): value for key, value in asciiTable().items()}
    plain = ""
    x = 0
    while isSmaller(x, len(binaryEncoded)):
        lengthOfBinEncodedNum = int(binaryEncoded[x])
        begInd = sumAlgB10(x, 1)
        endInd = sumAlgB10(begInd, lengthOfBinEncodedNum)
        ascii = str(fromBin(binaryEncoded[begInd:endInd]))
        plain += table[ascii]
        x = sumAlgB10(x, sumAlgB10(lengthOfBinEncodedNum, 1))
    return plain


def toBin(num: str) -> str:
    quotient, rem = divAlgB10(num, 2)
    if isEqual(quotient, 0):
        return str(rem)
    return toBin(quotient) + str(rem)

def fromBin(num:str) -> int:
    res = ""
    power = diffAlgB10(len(num), 1, None)
    if isSmaller(power, 0):
        return 0
    if isEqual(num[0], 1):
        return sumAlgB10(mod_pow(2, power, 1024), fromBin(num[1:]))
    else:
        return sumAlgB10(0, fromBin(num[1:]))

# TEST
# print(sqrt_int_part(2, 7))
# print(mod_pow(4123123213123, 123123123, 500))
# print(mod_pow_v2(4123123213123123, 123123123123213, 500))
# print(multAlgB10("1232", 1))
# print(fromBin("1111111"))

