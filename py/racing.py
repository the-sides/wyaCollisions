from Crypto.Hash import SHA256 as shaAlg

bitsN = 16

def sha(val):
    h = shaAlg.new(val)
    return h.digest()[:int(bitsN/8)]

def race(hashCount = 20000000):
    tortInd = 0
    hare = 1

    tortVal = b'sideshawkin1'
    tort = sha(tortVal)

    hareVal = tort
    hare = sha(tort)

    count = 0
    history = []
    for i in range(hashCount):
        tortVal = tort
        hareVal = sha(hare)
        tort = sha(tortVal)
        hare = sha(hareVal)

        if tort == hare:
            if "{}{}".format(tort, hare) in history:
                continue
            else:
                history.append("{}{}".format(tort, hare))

            if tortVal == hareVal: 
                continue
            count += 1


            print("{}) Found tort:{}     hare:{}".format(count, tort, hare))
            print("    From  val:{}         val:{}".format(tortVal, hareVal))
            
if __name__ == '__main__':
    race()

