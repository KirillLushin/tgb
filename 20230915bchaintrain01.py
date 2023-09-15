import hashlib

to_hash = input()

nonce = 0
for i in range(1,4):
    tmp = (to_hash + str(nonce)).encode()
    hash = hashlib.sha256(tmp).hexdigest()
    if hash[0:1] == "0":
        print(nonce)

    if hash[0:2] == "00":
        print(nonce)

    if hash[0:3] == "000":
        print(nonce)
        break
    else:
        i += 1


