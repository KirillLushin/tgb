import hashlib

to_hash = input().encode()

hash = hashlib.sha256(to_hash).hexdigest()

print(hash)