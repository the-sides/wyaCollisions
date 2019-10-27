'''  
Students: Jacob Sides and Ben Hawkin
Date:     Oct 26th, 2019
Purpose:  Use Tortoise and Hare algorith for cycle detection to find a collison point 
            at the start of cycle. The collision will be the value before entering the 
            cycle and the last element before restarting the cycle. 
'''

from Crypto.Hash import SHA256 as shaAlg
import time, datetime, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', nargs=1, type=int, default=32, help='Bits to match')
args = parser.parse_args()

try:
    bitsN = int(args.b[0])
except:
    bitsN = args.b

startingValue = b'sideshawkin'

def sha(val, partial = True):
    h = shaAlg.new(val)
    if partial:
        return h.digest()[:int(bitsN/8)]
    else:
        return h.digest()

def race():
    tortVal = startingValue
    tort = sha(tortVal)

    hareVal = tort
    hare = sha(tort)

    i = 0
    while tort != hare:
        tortVal = tort
        tort = sha(tortVal)

        hareVal = sha(hare)
        hare = sha(hareVal)
        i += 1

    # This finds the first collision value for the Tortoise 
    tort = startingValue
    while tort != hare:
        tortVal = tort
        tort = sha(tortVal)
        hare = sha(hare)

    # Put the hare one step ahead of tortoise to find where the cycle loops back around
    hare = sha(tort)
    while tort != hare:
        hareVal = hare
        hare = sha(hareVal)


    print("{}) Hashed tort:{}     hare:{}\n\n".format(i, tort, hare))
    return i, (tortVal, hareVal)
            
if __name__ == '__main__':
    startTime = time.time()
    print("Race Started:  Time: {}".format(str(datetime.datetime.now())))

    #  Collision Found
    count, collides = race()
    endTime = time.time()
    duration = endTime - startTime
    endTime = str(datetime.datetime.now()) # for presentation purposes

    print("Race Finished: Time: {}    for {} seconds \n Collisions found for {} bits after {} iterations".format(endTime, duration, bitsN, count))
    
    # for val in collides:
    print("h({}) = {}".format(collides[0], sha(collides[0])))
    print("h({}) = {}".format(collides[1], sha(collides[1])))

    # for val in collides:
    print("h({}) = {}".format(collides[0], sha(collides[0], False)))
    print("h({}) = {}".format(collides[1], sha(collides[1], False)))

