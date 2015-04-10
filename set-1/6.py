from __future__ import division
import sys, math
Three = __import__('3')

def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bin(ord(ch1) ^ ord(ch2))[2:].count('1') for ch1, ch2 in zip(s1, s2))

s1 = 'this is a test'
s2 = 'wokka wokka!!!'

print hamming_distance(s1, s2)

data = ''
with open ("6.txt") as f:
    data = f.read()

data = data.decode('base64')

ham_keys = []
for keysize in xrange(2,40):
    s1 = data[:keysize]
    s2 = data[keysize:keysize*2]
    h = hamming_distance(s1, s2) 
    ham_keys.append((h / keysize, keysize))

sorted_ham_keys = sorted(ham_keys, key=lambda x: x[0])
print sorted_ham_keys

def block_string(n):
    split = [data[i:i+n] for i in range(0, len(data), n)]
    blocks = []
    for i in xrange(len(split[0])):
        tmp = ''
        for x in split:
            if i < len(x):
                tmp += x[i]
        blocks.append(tmp)
    return blocks

def unblock_string(arr):
    ans = ''
    for i in xrange(len(arr[0])):
        s = ''
        for x in arr:
            if i < len(x):
                s += x[i]
        ans += s
    return ans

def decrypt(n):
    size = sorted_ham_keys[n][1]
    blocks = block_string(size)
    # print blocks

    ans = []
    for b in blocks:
        s = Three.single_byte_xor_cipher(b.encode('hex'))
        # print s
        ans.append(s)

    print unblock_string(ans)

avg = 0
for i in xrange(4):
    # decrypt(i)
    avg += sorted_ham_keys[i][1]
avg /= 4

# decrypt(int(math.ceil(avg)))
# decrypt(int(math.floor(avg)))