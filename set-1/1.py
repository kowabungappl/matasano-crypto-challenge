hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hex_to_b64(hex_string):
    return hex_string.decode('hex').encode('base64')

print hex_to_b64(hex_string)