from Crypto.Hash import SHA256 as shaAlg

def sha(val):
    h = shaAlg.new(val)
    return h.digest()

def race():
    hashCount = 2000
    tortInd = 0
    hare = 1

    tort = sha(b'sideshawkin')
    hare = sha(tort)

    for i in range(hashCount):
        pretort = tort[0]
        prehare = hare[0]
        tort = sha(tort[:2])
        hare = sha(sha(hare[:2]))
        if tort[0] == hare[0]:
            print("Found tort:{}     hare:{}")
            print("From  tort:{}     hare:{}")
            

