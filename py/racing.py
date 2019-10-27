from Crypto.Hash import SHA256 as shaAlg

bitsN = 16

def sha(val):
    h = shaAlg.new(val)
    return h.digest()[:int(bitsN/8)]

def race(hashCount = 20000000):
    tortVal = b'ssideshawk'
    tort = sha(tortVal)

    hareVal = tort
    hare = sha(tort)

    misses = 0
    count = 0
    collides = 0
    seenN = 0
    seen = {}
    history = []
    found = []
    for i in range(hashCount):
        tortVal = tort
        hareVal = sha(hare)
        tort = sha(tortVal)
        hare = sha(hareVal)

        if str(hare) in seen.keys():
            print('leader computed before {} times:{}'.format(hare, seen[str(hare)]))
            seen[str(hare)] += 1
        else:
            print("hashed {}:{} ".format(tort, hare))
            seen[str(hare)] = 0
            # seen.append(hare)
            
        if tort == hare:
            count += 1
            if tortVal == hareVal: 
                print('cycle found (same val)')
                print("Misses:{}  count:{} true collides:{}    m/c:{}".format( misses, count, collides, misses/count))
                continue

            if "{}{}".format(tort, hare) in history:
                print("{}:{} skipped bc of history".format(tort, hare))
                continue
            else:
                print("{}:{} added to history".format(tort, hare))
                history.append("{}{}".format(tort, hare))
                collides += 1


            found.append((tortVal, hareVal))
            print("{}) Found tort:{}     hare:{}".format(count, tort, hare))
            print("    From  val:{}         val:{}".format(tortVal, hareVal))
        else:
            misses += 1
    return count, collides, misses
            
if __name__ == '__main__':
    count, collides, misses = race()
    print("Race Finished")
    print("Misses:{}  count:{} true collides:{}", misses, count, collides)

