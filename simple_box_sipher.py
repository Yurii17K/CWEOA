import time

from Diffie_Hellman_key_exchange import defHelExchange
from div_alg import divAlgB10
from mult_alg import multAlgB10
from sum_alg import sumAlgB10
from utils import isSmaller, toBin


def demoSbox(B: str):
    K = defHelExchange(33, 54, 71, (15, 44), 20)
    keyList = convertKeyTo4BlocksOf32(K)
    table, invTable = generateSBoxTable()
    xorLT = initXorLookup()

    C = sbs(B, keyList, table, xorLT)
    decoded = decodeSbs(C, keyList, invTable, xorLT)
    print("Decoded string: ", str(decoded))
    pass


def sbs(B: str, K: list, sboxTable: dict, xorLT: dict):
    print("Started encoding for: ", B)
    state = B

    for x in range(3):
        state = xor(state, K[x], xorLT)
        state = sbox(state, sboxTable)
        state = perm(state)

    state = xor(state, K[3], xorLT)
    return state


def xor(num1: str, key: str, xorLT: dict):
    res = ""
    if len(num1) < 32:
        raise Exception("Messaged has been compromised")

    for x in range(32):
        res += xorLT[(num1[x], key[x])]
    return res


def decodeSbs(C: str, K: list, invTable: dict, xorLT: dict) -> int:
    print("Started decoding for: ", C)
    state = C
    state = xor(state, K[3], xorLT)
    for x in [2, 1, 0]:
        state = invPerm(state)
        state = invSbox(state, invTable)
        state = xor(state, K[x], xorLT)
    return state


def convertKeyTo4BlocksOf32(K: tuple):
    K = sumAlgB10(K[0], K[1])
    K = str(K)
    while isSmaller(len(K), 128):
        print("Converting keys...")
        K = toBin(K)
    K = K[:128]
    K1 = K[:32]
    K2 = K[32:64]
    K3 = K[64:96]
    K4 = K[96:128]
    return [K1, K2, K3, K4]


def generateSBoxTable() -> dict:
    table = {}
    invTable = {}
    items = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    itemsShuffled = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in range(10):
        index = divAlgB10(multAlgB10(x, int(time.time())), 10)[1]
        itemsShuffled[x], itemsShuffled[index] = itemsShuffled[index], itemsShuffled[x]
    for x in range(10):
        table[items[x]] = itemsShuffled[x]
        invTable[itemsShuffled[x]] = items[x]
    return table, invTable


def initXorLookup():
    xor_table = {}
    for i in range(10):
        for j in range(10):
            xor_table[(str(i), str(j))] = str(i ^ j)
    return xor_table


def sbox(B: str, table: dict) -> str:
    P = ""
    if len(B) < 32:
        raise Exception("Messaged has been compromised")

    for x in range(32):
        P += table[B[x]]
    return P


def invSbox(B: str, invTable: dict):
    if len(B) < 32:
        raise Exception("Messaged has been compromised")
    P = ""
    for x in range(32):
        P += invTable[B[x]]
    return P


def perm(B: str):
    P = B[16:24] + B[:8] + B[24:32] + B[8:16]
    if len(P) < 32:
        raise Exception("Messaged has been compromised")
    return P


def invPerm(C: str):
    P = C[8:16] + C[24:32] + C[:8] + C[16:24]
    if len(P) < 32:
        raise Exception("Messaged has been compromised")
    return P

# demoSbox(12345678912345678912345678912345)
