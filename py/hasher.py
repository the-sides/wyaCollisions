from Crypto.Hash import SHA256 as sha

H = sha.new()
H.update(b'deadbeef')
hashes = []

hashCount = 500000
print('Hashing {} times', hashCount)

for i in range(hashCount):
    H = sha.new(b'deadbeef')
    hashes.append(H.digest())

print("All hashes computed")
print("Time to access hashes")

for i in range(hashCount):
    hashes[i]