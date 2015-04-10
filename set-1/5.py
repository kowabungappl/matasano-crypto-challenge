string = "Burning 'em, if you ain't quick and nimble\n" + "I go crazy when I hear a cymbal"
key = 'ICE'

def encrypt(string, key):
    extended_key = key * ((len(string) / len(key)) + 1)
    return ''.join((chr(ord(a)^ord(b))) for a,b in zip(string, extended_key)).encode('hex')

print encrypt(string, key)
