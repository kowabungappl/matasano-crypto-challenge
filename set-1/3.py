from __future__ import division
import math

hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def single_byte_xor_cipher(hex_string):
    string = hex_string.decode('hex')

    ans = (0.0, '')
    for i in xrange(256):
        potential = ''.join((chr(ord(x) ^ i) for x in string))
        n = bhatt_coeff(potential)
        if n > ans[0]:
            ans = (n, potential)
    # print ans
    return ans[1]


def bhatt_coeff(string):

    ENGLISH_FREQUENCIES = {
        'E' : .1202,
        'T' : .0910,
        'A' : .0812,
        'O' : .0768,
        'I' : .0731,
        'N' : .0695,
        'S' : .0628,
        'R' : .0602,
        'H' : .0592,
        'D' : .0432,
        'L' : .0398,
        'U' : .0288,
        'C' : .0271,
        'M' : .0261,
        'F' : .0230,
        'Y' : .0211,
        'W' : .0209,
        'G' : .0203,
        'P' : .0182,
        'B' : .0149,
        'V' : .0111,
        'K' : .0069,
        'X' : .0017,
        'Q' : .0011,
        'J' : .0010,
        'Z' : .0007
    }

    string = string.upper()
    freqs = {}
    for c in string:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1

    for c in freqs.keys():
        freqs[c] /= len(string)

    score = 0.0
    for c in ENGLISH_FREQUENCIES:
        if c not in freqs:
            freqs[c] = 0.0
        score += math.sqrt(freqs[c] * ENGLISH_FREQUENCIES[c])

    return score

print single_byte_xor_cipher(hex_string)