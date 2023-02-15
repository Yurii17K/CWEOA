
from Diffie_Hellman_key_exchange import defHelExchange
from diff_alg import diffAlgB10
from div_alg import divAlgB10
from mult_alg import multAlgB10
from simple_box_sipher import sbs, decodeSbs, generateSBoxTable, convertKeyTo4BlocksOf32, initXorLookup
from sum_alg import sumAlgB10
from utils import toAsciiToBin, fromBinToAsciiToPlain
from utils_alg import isEqual


def hybrid_system():
    print("Initialization of a hybrid system....")
    sharedKey = defHelExchange(312345, 123214, 21269, (15467, 13551), 148)
    # sharedKey = defHelExchange(312345, 123214, 17, (14, 55), 20) #quicker
    keyList = convertKeyTo4BlocksOf32(sharedKey)
    xorLT = initXorLookup()
    print("Initialization finished!")

    enableAi = initAi()

    print("\n Simulate a conversation by writing messages.")
    playGame(keyList, xorLT, enableAi)


def initAi() -> bool:
    print("\n [EXPERIMENTAL FEATURE] Make sure to read the instructions first!!!"
          "\n This might slow down the responses!!"
          "\n Do you want to enable Chat GPT for receiving responses?"
          "\n You can alter this later at any moment by writing 'ENABLE AI' or 'DISABLE AI'")

    dec = input("\n Type YES is yeah, and NO if you want to proceed without changes: ")

    if isEqual(dec, "YES"):
        print("\n AI has been ENABLED.")
        return True

    return False


def generateResponse(openAiEnabled: bool, decodedMessage: str) -> str:
    if not openAiEnabled:
        return "Thanks for your message '" + decodedMessage + "'!"

    # is not global so that the system works without installing additional dependencies
    import openai

    openai.api_key = "YOU CHAT GPT API KEY"
    res = openai.Completion.create(
        engine="text-davinci-003",
        prompt=decodedMessage,
        temperature=0.5,  # Level of creativity in the response
        max_tokens=50,  # Maximum tokens in the prompt AND response
        n=1,  # The number of completions to generate
        stop=None
    )
    return str(res.choices[0].text)


def playGame(keyList: list, xorLT: dict, openAiEnabled: bool):
    print(" Welcome! To stop a game write 'bye' to Bob. Enjoy!")

    while True:
        Ma = input("\n Alice: ")
        if isEqual(Ma, "bye"):
            break
        if isEqual(Ma, "ENABLE AI"):
            openAiEnabled = True
            print("\n AI has been ENABLED.")
            continue
        if isEqual(Ma, "DISABLE AI"):
            openAiEnabled = False
            print("\n AI has been DISABLED.")
            continue

        print("\n Alice is encoding her message...")
        encodedChunks, invTable, numOfFillers = encodeMessage(Ma, keyList, xorLT)
        print("Alice is sending her message...")

        print("\n Bob has received a message... Bob is decoding Alice's message..")
        decodedMessage = decodeChunks(encodedChunks, keyList, invTable, numOfFillers, xorLT)

        print("Bob is writing his response..")
        Mb = generateResponse(openAiEnabled, decodedMessage)

        print("Bob is encoding his response...")
        encodedChunks, invTable, numOfFillers = encodeMessage(Mb, keyList, xorLT)
        print("Bob is sending his response..")

        print("\n Alice has received Bob's reponse... Alice is decoding Bob's response...")
        decodedMessage = decodeChunks(encodedChunks, keyList, invTable, numOfFillers, xorLT)
        print("\n Bob: " + decodedMessage)

    print("\n See you!")


def encodeMessage(B: str, keyList: list, xorLT: dict):
    table, invTable = generateSBoxTable()
    B = toAsciiToBin(B)

    chunks, numOfFillers = divideIntoChunks(B)
    for x in range(len(chunks)):
        chunks[x] = sbs(chunks[x], keyList, table, xorLT)

    return chunks, invTable, numOfFillers


def decodeChunks(encodedChunks: list, keyList: list, invTable: dict, numOfFillers: int, xorLT: dict):
    msg = ""
    for x in range(len(encodedChunks)):
        msgChunk = decodeSbs(encodedChunks[x], keyList, invTable, xorLT)
        if isEqual(x, diffAlgB10(len(encodedChunks), 1, None)):
            msgChunk = msgChunk[:diffAlgB10(32, numOfFillers, None)]
        msg += msgChunk
    return fromBinToAsciiToPlain(msg)


def divideIntoChunks(B):
    numOfFillers = 0
    chunks = []

    iters = divAlgB10(len(B), 32)
    if not isEqual(iters[1], 0):
        iters = sumAlgB10(iters[0], 1)

    for x in range(iters):
        begInd = multAlgB10(x, 32)
        endInd = sumAlgB10(begInd, 32)
        chunk = B[begInd: endInd]
        if isEqual(x, diffAlgB10(iters, 1, None)):
            chunk, numOfFillers = addFillers(chunk)
        chunks.append(chunk)
    return chunks, numOfFillers


def addFillers(B: str) -> tuple[str, int]:
    size = len(B)
    fillers = ""
    for x in range(diffAlgB10(32, size, None)):
        fillers += '0'
    return B + fillers, diffAlgB10(32, size, None)


# TEST
# print(encodeMessage(68923652689758946238976528936537658352376748952634856238912312312756289346589236589367547))
# print(isEqual("012312"[0], '0'))

hybrid_system()
