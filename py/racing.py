from Crypto.Hash import SHA256 as shaAlg

bitsN = 32
startingValue = b'sideshawkin'

def sha(val, partial = True):
    h = shaAlg.new(val)
    if partial:
        return h.digest()[:int(bitsN/8)]
    else:
        return h.digest()

def race(hashCount = 2000000000):
    tortVal = startingValue
    tort = sha(tortVal)

    hareVal = tort
    hare = sha(tort)

    for i in range(hashCount):
        tortVal = tort
        tort = sha(tortVal)

        hareVal = sha(hare)
        hare = sha(hareVal)

            
        if tort == hare:

            # Thanks wikipedia
            # This finds the first collision value for the Tortise 
            tort = startingValue
            while tort != hare:
                tortVal = tort
                tort = sha(tortVal)
                hare = sha(hare)

            # Put the hare one step ahead of tortise to find where the cycle loops back around
            hare = sha(tort)
            while tort != hare:
                hareVal = hare
                hare = sha(hareVal)


            print("{}) Found tort:{}     hare:{}".format(i, tort, hare))
            print("    From  val:{}         val:{}".format(tortVal, hareVal))
            return i, (tortVal, hareVal)
            
if __name__ == '__main__':
    count, collides = race()
    print("Race Finished: Collisions found for {} bits after {} iterations".format(bitsN, count))
    
    # for val in collides:
    print("h({}) = {}".format(collides[0], sha(collides[0])))
    print("h({}) = {}".format(collides[1], sha(collides[1])))

    # for val in collides:
    print("h({}) = {}".format(collides[0], sha(collides[0], False)))
    print("h({}) = {}".format(collides[1], sha(collides[1], False)))

