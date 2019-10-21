from Crypto.Hash import SHA256 as sha
from math import ceil
import pprint as pp

def compByte(b1, b2):
    # Comparing the size of the length of binary bits will already determine the 8-L amount of bits.
    xor = b1 ^ b2
    # print('comparing:  ', b1, b2)
    # print('binary form: {}({}) {}({})'.format(bin(b1), len(bin(b1))-2, bin(b2), len(bin(b2))-2))
    # print('XOR output: ', bin(xor))

    # bin(byte) will produce the string output of a bits in the notation '0b00110011' 
    #   so the first 2 chars unused. If 2 bytes share a smaller length, then the 
    #   first bits collide with the fact that they're both 0.
    b1N = len(bin(b1)) - 2
    b2N = len(bin(b2)) - 2
    
    # Bits matching (leading zeros if both aren't using all 8 bits)
    bits = 8 - b1N if b1N > b2N else 8 - b2N

    if b1N == b2N:
        # Xor starts where bits differ, so look at the length of the xor.
        if xor == 0: 
            bits = 8
        else:
            bits = 8 - int(len(bin(xor))-2)

    # print('leading bits similar: {}'.format(bits))

    return bits

# Will compare last hash with all those before
def compHash(hash1, hash2):
    bits = 0
    for i, char1 in enumerate(hash1):
        bits += compByte(char1, hash2[i])
        if (bits % 8 != 0) | (bits == 0):
            # print("bits collided: {}".format(bits))
            break
        else:
            if i == 3:
                print('we found a duplicate value?')
            else:
                print("STILL GOING!")

    return bits

    
def debugCompByte():
    H = sha.new()
    H.update(b'sideshawkin')
    h0 = H.digest()
    print(h0[0])
    for g in range(len(h0)-1):
        compByte(h0[g], h0[g+1])
    

# Once a handful of hashes have been calculated, this is the race that will compare hash outcomes
def startRace(h):
    collisions = []
    sameVals = []
    tortInd = 0
    hareInd = 1
    tort = h[tortInd]
    hare = h[hareInd]
    for i in range(int(len(h)/2)):

        tortInd += 1
        hareInd += 2
        tort = h[tortInd]
        hare = h[hareInd]

        if tort == hare:
            sameVals.append((tortInd, h[tortInd-1], hareInd, h[hareInd-1]))
            continue
        
        if compHash(tort, hare) >= 16:
            newHash = sha.new(h[tortInd-1])
            recomputedT = newHash.digest()
            newHash = sha.new(h[hareInd-1])
            recomputedH = newHash.digest()
            pair = ({
                    'valueT': h[tortInd-1],
                    'hashedT': h[tortInd],
                    'computedT': recomputedT
                },
                {
                    'valueH': h[hareInd-1],
                    'hashedH': h[hareInd],
                    'computedH': recomputedH

                })

            collisions.append(pair)
            print("Hash collision of 16 MSB bits")
            break
            
    return collisions,sameVals


hashes = []

hashCount = 200000
bitTarget = 16
byteTarget = ceil(bitTarget/8)
print('Hashing {} times', hashCount)
print('byteTarget {}', byteTarget)

prev = b'sideshawkin'
for i in range(hashCount):
    H = sha.new(prev)
    prev = H.digest()[:byteTarget]
    hashes.append(prev)
    

print("{} hashes computed".format(hashCount))
print("Looking for collisions...")

collides, sameVals = startRace(hashes)

print("Finished searching for collisions...")
print("Found: ")
for val in collides:
    pp.pprint(val[0])
    pp.pprint(val[1])

for same in sameVals:
    pp.pprint(same)

