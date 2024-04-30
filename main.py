# This is a sample Python script.

Sbox = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]

# Rcon[] is 1-based, so the first entry is just a place holder
Rcon = [
    0x00000000,
    0x01000000, 0x02000000, 0x04000000, 0x08000000,
    0x10000000, 0x20000000, 0x40000000, 0x80000000,
    0x1B000000, 0x36000000, 0x6C000000, 0xD8000000,
    0xAB000000, 0x4D000000, 0x9A000000, 0x2F000000,
    0x5E000000, 0xBC000000, 0x63000000, 0xC6000000,
    0x97000000, 0x35000000, 0x6A000000, 0xD4000000,
    0xB3000000, 0x7D000000, 0xFA000000, 0xEF000000,
    0xC5000000, 0x91000000, 0x39000000, 0x72000000,
    0xE4000000, 0xD3000000, 0xBD000000, 0x61000000,
    0xC2000000, 0x9F000000, 0x25000000, 0x4A000000,
    0x94000000, 0x33000000, 0x66000000, 0xCC000000,
    0x83000000, 0x1D000000, 0x3A000000, 0x74000000,
    0xE8000000, 0xCB000000, 0x8D000000
]

InvSbox = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Does the XOR operations
def ffAdd(x, y):
    # Use a breakpoint in the code line below to debug your script.
    return x ^ y


# Does the Finite Field Multiplication
def ffMultiply(x, y):
    multi = 0
    while y >= 1:
        if (y & 0x01) == 1:
            multi = multi ^ x
        x = xtime(x)
        y = y >> 1

    return multi


def xtime(x):
    x = x << 1
    if (x & 0x100) > 0:
        x = x ^ 0x11b

    return x


def subByte(state):
    for i in range(4):
        state[i] = subWord(state[i])
    return state


# fn(u8[4]) -> u8[4]
# fn(u32) -> u32


def rotWord(state):
    return state[1:] + state[0:1]


def subWord(word):
    empty_word = [0,0,0,0]
    for i in range(len(word)):
        byte1, byte2 = divmod(word[i], 0x10)
        empty_word[i] = Sbox[byte1][byte2]
    return empty_word


'''def rotWord(word):
    temp = word & 0xff
    word = word >> 8
    word = word & 0xffffff
    word |= temp << 16
    return word'''

'''def state_to_byte(state):
    return [(state >> 8 * (3 - i)) & 0xff for i in range(4)]


def byte_list_to_int(w):
    ret = 0
    for byte in w:
        ret <<= 8
        ret |= 8
    return ret'''


# Press the green button in the gutter to run the script.


def word(param, param1, param2, param3):
    pass


def key_expantion(key):
    Nk = len(key) // 4
    Nb = 4
    key_length = len(key) * 8
    if key_length == 128:
        Nr = 10
    elif key_length == 192:
        Nr = 12
    elif key_length == 256:
        Nr = 14
    else:
        print("Does not mach the key bit option")
    i = 0
    w = [[0, 0, 0, 0] for i in range((Nr + 1) * Nb)]
    while i < Nk:
        w[i] = [key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]]
        # print(str_from_state(w))
        i = i + 1

    i = Nk
    while i < Nb * (Nr + 1):
        temp = w[i - 1]
        if i % Nk == 0:
            temp = subWord(rotWord(temp))

            rconOperation = Rcon[i // Nk]
            temp[0] = temp[0] ^ Rcon[i // Nk] >> 24
            temp[1] = temp[1] ^ divmod(rconOperation, 0x10000)[1]
            temp[2] = temp[2] ^ divmod(rconOperation, 0x1000)[1]
            temp[3] = temp[3] ^ divmod(rconOperation, 0x100)[1]
            # ffAdd(Rcon[i // Nk], temp)


        elif Nk > 6 and i % Nk == 4:
            temp = subWord(temp)

        w_value = w[i - Nk]
        w[i] = [ffAdd(w_value[j], temp[j]) for j in range(4)]
        i = i + 1

    return w


def add_round_key(state, key_expanded, round_number):
    round_key = key_expanded[round_number * 4:round_number * 4 + 4]
    """for i in range(4):
        for j in range(4):
            state[i][j] = round_key[i][j]
    return state"""
    for i in range(len(state)):
        state[i] = [state[i][j] ^ round_key[i][j] for j in range(4)]


def shiftRows(state):
    state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
    state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
    state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]


def mixColumns(state):
    for i in state:
        ColOperation(i)


def ColOperation(col):
    place_holder_for_col_0 = col[0]
    xor = col[0] ^ col[1] ^ col[2] ^ col[3]
    col[0] ^= xor ^ xtime(col[0] ^ col[1])
    col[1] ^= xor ^ xtime(col[1] ^ col[2])
    col[2] ^= xor ^ xtime(col[2] ^ col[3])
    col[3] ^= xor ^ xtime(place_holder_for_col_0 ^ col[3])


# Shitch col with variables
'''def ColOperation(state):
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for col in range(4):
        result[0][col] = ffAdd(ffAdd(ffAdd(ffMultiply(0x02, state[0][col]), ffMultiply(0x03, state[1][col])),state[2][col]), state[3][col])
        result[1][col] = ffAdd(ffAdd(ffAdd(state[0][col], ffMultiply(0x02, state[1][col])),ffMultiply(0x03, state[2][col])), state[3][col])
        result[2][col] = ffAdd(ffAdd(ffAdd(state[0][col], state[1][col]), ffMultiply(0x02, state[2][col])),ffMultiply(0x03, state[3][col]))
        result[3][col] = ffAdd(ffAdd(ffAdd(ffMultiply(0x03, state[0][col]), state[1][col]), state[2][col]),ffMultiply(0x02, state[3][col]))
    return result'''


def aes_cipher(plaintext, key):
    key_length = len(key) * 4
    if key_length == 128:
        Nr = 10
    elif key_length == 192:
        Nr = 12
    elif key_length == 256:
        Nr = 14
    else:
        print("Does not mach the key bit option")

    state = state_from_str(plaintext)
    key_byte = bytes_from_str(key)
    keyExpanded = key_expantion(key_byte)
    round_number = 0
    add_round_key(state, keyExpanded, round_number)


    for round_number in range(1, Nr):
        subByte(state)

        shiftRows(state)


        mixColumns(state)


        add_round_key(state, keyExpanded, round_number)


    subByte(state)

    shiftRows(state)


    round_number = Nr
    add_round_key(state, keyExpanded, round_number);

    cipher = str_from_state(state)
    return cipher


def inv_shiftRows(state):
    state[1][1], state[2][1], state[3][1], state[0][1] = state[0][1], state[1][1], state[2][1], state[3][1]
    state[2][2], state[3][2], state[0][2], state[1][2] = state[0][2], state[1][2], state[2][2], state[3][2]
    state[3][3], state[0][3], state[1][3], state[2][3] = state[0][3], state[1][3], state[2][3], state[3][3]
    return


def inv_subByte(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = InvSbox[state[i][j]]
    return state

#Simple matrix multiplication
def inv_ColOperations(col):
    opCol_02 = xtime(xtime(col[0] ^ col[2]))
    opCol_13 = xtime(xtime(col[1] ^ col[3]))
    col[0] ^= opCol_02
    col[1] ^= opCol_13
    col[2] ^= opCol_02
    col[3] ^= opCol_13


def inv_mixColumns(state):
    for i in state:
        inv_ColOperations(i)
    mixColumns(state)


def aes_InvCypher(cipher, key):
    key_length = len(key) * 4
    if key_length == 128:
        Nr = 10
    elif key_length == 192:
        Nr = 12
    elif key_length == 256:
        Nr = 14
    else:
        print("Does not mach the key bit option")

    state = state_from_str(cipher)
    key_byte = bytes_from_str(key)
    keyExpanded = key_expantion(key_byte)


    round_number = Nr
    add_round_key(state, keyExpanded, round_number)

    for round_number in range(Nr - 1, 0, -1):
        inv_shiftRows(state)
        inv_subByte(state)
        add_round_key(state, keyExpanded, round_number)
        inv_mixColumns(state)

    inv_shiftRows(state)
    inv_subByte(state)
    round_number = 0
    add_round_key(state, keyExpanded, round_number)

    plaintext = str_from_state(state)
    return plaintext


if __name__ == '__main__':
    # print(hex(ffAdd(0x57, 0x83)))
    # print(hex(xtime(0x57)))
    # print(hex(ffMultiply(0x57, 0x13)))

    # print(hex(subWord(0x00102030)))
    w = 0x09cf4f3c
    # w = [
    #     (w >> 24) & 0xff,
    #     (w >> 16) & 0xff,
    #     (w >> 8) & 0xff,
    #     w & 0xff,
    # ]

    '''w = rotWord(int_to_byte_list(0x09cf4f3c))
    for i in w:
        print(f"{i:02x}", end="")
    print()

    w = subWord(int_to_byte_list(0x00102030))
    for i in w:
        print(f"{i:02x}", end="")
    print()'''


    def state_from_str(text):
        return [[int(text[(i * 4 + j) * 2:(i * 4 + j) * 2 + 2], 16) for j in range(4)] for i in range(4)]


    def bytes_from_str(text):
        return [int(text[i * 2:i * 2 + 2], 16) for i in range(len(text) // 2)]


    def str_from_state(state):
        ret = ""
        for col in state:
            for val in col:
                ret += f"{val:02x}"
        return ret


    plaintext = '6a7d6198b0c7fe884ee0cec9ce36a01a'
    # print(state_from_str(plaintext))
    # print(str_from_state(state_from_str(plaintext)))
    key = 'da8faabbeebb9de0c1adfcdc487533f17301be59951ca6db'
    print(bytes_from_str(key))
    correct_cipherOutput = '8ea2b7ca516745bfeafc49904b496089'
    cipher = aes_cipher(plaintext, key)
    print(str_from_state(state_from_str(cipher)))
    decryption = "fdbf18faaf6f0b8fc5dc3edb5d9f6074"
    decrypted_output = aes_InvCypher(decryption, key)
    print(str_from_state(state_from_str(decrypted_output)))

    if cipher != correct_cipherOutput:
        print("Description Output does not match")
    else:
        print("Incryption Pass")

    if plaintext != decrypted_output:
        print("Description Output does not match")
    else:
        print("Decryption Pass")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
