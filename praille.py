# Praille.
# Python Braille related functions.
#
# Copyright (C) 2020, Ty Gillespie. All rights reserved.
# MIT License.

"""We currently only support 8-dot computer Braille.
More are planned.
"""

# The Braille table. A 0 means the characters doesn't exist, a 1 means it does.
braille_table = {
    " ": "00000000",
    ",": "01000000",
    ".": "01001100",
    ":": "01001000",
    ";": "01100000",
    "'": "00100000",
    "?": "01100100",
    "!": "01101000",
    "$": "0001000001110000",
    "%": "0001010000101100",
    "a": "10000000",
    "b": "11000000",
    "c": "10010000",
    "d": "10011000",
    "e": "10001000",
    "f": "11010000",
    "g": "11011000",
    "h": "11001000",
    "i": "01010000",
    "j": "01011000",
    "k": "10100000",
    "l": "11100000",
    "m": "10110000",
    "n": "10111000",
    "o": "10101000",
    "p": "11110000",
    "q": "11111000",
    "r": "11101000",
    "s": "01110000",
    "t": "01111000",
    "u": "10100100",
    "v": "11100100",
    "w": "01011100",
    "x": "10110100",
    "y": "10111100",
    "z": "10101100",
    "A": "10000010",
    "B": "11000010",
    "C": "10010010",
    "D": "10011010",
    "E": "10001010",
    "F": "11010010",
    "G": "11011010",
    "H": "11001010",
    "I": "01010010",
    "J": "01011010",
    "K": "10100010",
    "L": "11100010",
    "M": "10110010",
    "N": "10111010",
    "O": "10101010",
    "P": "11110010",
    "Q": "11111010",
    "R": "11101010",
    "S": "01110010",
    "T": "01111010",
    "U": "10100110",
    "V": "11100110",
    "W": "01011110",
    "X": "10110110",
    "Y": "10111110",
    "Z": "10101110",
    "1": "10000001",
    "2": "11000001",
    "3": "10010001",
    "4": "10011001",
    "5": "10001001",
    "6": "11010001",
    "7": "11011001",
    "8": "11001001",
    "9": "01010001",
    "0": "01011001",
}


def decode(string):
    """Decodes from Braille to readable English."""
    out = ""
    chunks, chunk_size = len(string), 8
    for i in range(0, chunks, chunk_size):
        for key, value in braille_table.items():
            if value == string[i : i + chunk_size]:
                out += key
                continue
    return out


def encode(string):
    """Encode English to a Braille string."""
    out = ""
    for s in string:
        out += braille_table[s]
    return out
