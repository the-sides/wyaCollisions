from Crypto.Hash import SHA256 as sha

def compByte(b1, b2):
    # Comparing the size of the length of binary bits will already determine the 8-L amount of bits.
    print(b1, b2)
    print(bin(b1), bin(b2))
    xor = b1 ^ b2
    print(bin(xor))
    bits = len(bin(b2)) - len(bin(xor))
    print('leading bits similar: {}'.format(bits))
    # for i in range(8):
    #     for j in range(8):

    
H = sha.new()
H.update(b'deadbeefadfbadjfhbnsidfhjbnidsfhjnbv')
h0 = H.digest()
print(h0[0])
for g in range(len(h0)-1):
    compByte(h0[g], h0[g+1])
    

hashes = []

hashCount = 50
print('Hashing {} times', hashCount)

for i in range(hashCount):
    H = sha.new(b'deadbeef')
    hashes.append(H.digest())

print("All hashes computed")
print("Time to access hashes")

for i in range(hashCount):
    hashes[i]


        

# Will compare last hash with all those before
def compHash(hash1, hash2):
    bits = 0
    for char1 in hash1:
        for char2 in hash2:
            if char1 != char2:
                break
            else:
                bits += 1
    return bits



