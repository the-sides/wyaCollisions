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
                print("{}:{} skipped bc of history".format(tort, hare))
                continue
            else:
                print("{}:{} added to history".format(tort, hare))
                history.append("{}{}".format(tort, hare))

            if tortVal == hareVal: 
                print('cycle found (same val)')
                continue
            count += 1


            print("{}) Found tort:{}     hare:{}".format(count, tort, hare))
            print("    From  val:{}         val:{}".format(tortVal, hareVal))
            
if __name__ == '__main__':
    race()

