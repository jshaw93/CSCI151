VALUES = {
    "a": 0, "b": 1, "c": 2,
    "d": 3, "e": 4, "f": 5, "g": 6,
    "h": 7, "i": 8, "j": 9, "k": 10,
    "l": 11, "m": 12, "n": 13, "o": 14,
    "p": 15, "q": 16, "r": 17, "s": 18,
    "t": 19, "u": 20, "v": 21, "w": 22,
    "x": 23, "y": 24, "z": 25, "A": 26,
    "B": 27, "C": 28, "D": 29, "E": 30,
    "F": 31, "G": 32, "H": 33, "I": 34,
    "J": 35, "K": 36, "L": 37, "M": 38,
    "N": 39, "O": 40, "P": 41, "Q": 42,
    "R": 43, "S": 44, "T": 45, "U": 46,
    "V": 47, "W": 48, "X": 49, "Y": 50,
    "Z": 51, " ": 52, "0": 53, "1": 54,
    "2": 55, "3": 56, "4": 57, "5": 58,
    "6": 59, "7": 60, "8": 61, "9": 62
}

REVERSE_VALUES = {
    0: "a", 1: "b", 2: "c", 3: "d",
    4: "e", 5: "f", 6: "g", 7: "h",
    8: "i", 9: "j", 10: "k", 11: "l",
    12: "m", 13: "n", 14: "o", 15: "p",
    16: "q", 17: "r", 18: "s", 19: "t",
    20: "u", 21: "v", 22: "w", 23: "x",
    24: "y", 25: "z", 26: "A", 27: "B",
    28: "C", 29: "D", 30: "E", 31: "F",
    32: "G", 33: "H", 34: "I", 35: "J",
    36: "K", 37: "L", 38: "M", 39: "N",
    40: "O", 41: "P", 42: "Q", 43: "R",
    44: "S", 45: "T", 46: "U", 47: "V",
    48: "W", 49: "X", 50: "Y", 51: "Z",
    52: " ", 53: "0", 54: "1", 55: "2",
    56: "3", 57: "4", 58: "5", 59: "6",
    60: "7", 61: "8", 62: "9"
}


def encrypt(message, key):
    index = 0
    encrypted_text = ''
    for i in message:
        chr_val = VALUES[i]
        key_val = VALUES[key[index]]
        calc = (chr_val + key_val) % 63
        encrypted_text += REVERSE_VALUES[calc]
        if index == len(key) - 1:
            index = 0
        else:
            index += 1
    return encrypted_text


def decrypt(cipher_text, key):
    index = 0
    decrypted_text = ''
    for i in cipher_text:
        chr_val = VALUES[i]
        key_val = VALUES[key[index]]
        calc = (chr_val - key_val) % 63
        decrypted_text += REVERSE_VALUES[calc]
        if index == len(key) - 1:
            index = 0
        else:
            index += 1
    return decrypted_text


if __name__ == '__main__':
    print('Test case: Using string of Hello World and key of Tim')
    print('Resulting cypher text should result in: "pmx3wbEwD3l"')
    cyphered = encrypt('Hello World', 'Tim')
    print(f'Cypher text: {cyphered},',
          "Match" if cyphered == 'pmx3wbEwD3l' else 'No Match')
    print('Decyphering "pmx3wbEwD3l" should result in: "Hello World"')
    decyphered = decrypt(cyphered, 'Tim')
    print(f'Decyphered text: {decyphered},',
          "Match" if decyphered == "Hello World" else "No Match")
