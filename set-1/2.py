hex_string1 = '1c0111001f010100061a024b53535009181c'
hex_string2 = '686974207468652062756c6c277320657965'

def fixed_xor(hex_string1, hex_string2):
    hex1 = hex_string1.decode('hex')
    hex2 = hex_string2.decode('hex')
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(hex1,hex2)).encode('hex')

print fixed_xor(hex_string1, hex_string2)