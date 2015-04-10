Three = __import__('3')

# Dictionary of most common words, https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt
d = [line.strip() for line in open('../google-10000-english.txt')]

# def detect_single_char_xor(file):
#     words = [line.strip() for line in open(file)]
#     ans = (0, '', '')
#     for w in words:
#         s = Three.single_byte_xor_cipher(w)
#         if len(s) > 0:
#             for x in s:
#                 count = 0
#                 arr = x.split(' ')
#                 for i in arr:
#                     if i in d:
#                         count += 1
#                 if count > ans[0]:
#                     ans = (count, n, x, w)
#     return ans

def detect_single_char_xor(file):
    words = [line.strip() for line in open(file)]
    ans = (0, '', '')
    for w in words:
        s = Three.single_byte_xor_cipher(w)
        # print s
        n = Three.bhatt_coeff(s)
        if n >= ans[0]:
            ans = (n, s, w)
    return ans

print detect_single_char_xor('4.txt')