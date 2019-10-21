from Crypto.Hash import SHA256 as sha

def compByte(b1, b2):
    # Comparing the size of the length of binary bits will already determine the 8-L amount of bits.
    print('comparing:  ', b1, b2)
    print('binary form:', bin(b1), bin(b2))
    xor = b1 ^ b2
    print('XOR output: ', bin(xor))
    bits = len(bin(b2)) - len(bin(xor))

    # bin(byte) will produce the string output of a bits in the notation '0b00110011' 
    #   so the first 2 chars unused. If 2 bytes share a smaller length, then the 
    #   first bits collide with the fact that they're both 0.
    b1N = len(bin(b1)) - 2
    b2N = len(bin(b2)) - 2
    longest = b1N if b1N > b2N else b2N
    shortest = b2N if b1N > b2N else b1N
    print('leading bits similar: {}'.format(8 - longest - shortest))
    # for i in range(8):
    #     for j in range(8):

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

    
H = sha.new()
H.update(b'sideshawkin')
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

# Once a handful of hashes have been calculated, this is the race that will compare hash outcomes
def startRace(h):
    tortInd = 0
    hareInd = 1
    tort = h[tortInd]
    hare = h[hareInd]
    for i in range(len(h)):

        tortInd += 1
        hareInd = 2
        tort = h[tortInd]
        hare = h[hareInd]
        if compHash(tort, hare) >= 16:
            print("Hash collision of 16 MSB bits")
            break





