import math

p = int(input())
q = int(input())

n = p*q
f = (p-1)*(q-1)
e = 1
d = 1
def gcd (f):
    e = 1
    while (1):
        if (math.gcd(e,f) ==1):
            break
        else:
            e+=1
    return e

def find_d (e, f):
    d = 1
    while (1):
        if ((e*d)%f == 1):
            break
        else:
            d+=1
            return d



print ("Public key: (", e, '\t', n, ')\n', "Private key: (", d, '\t', n, ')')

M = int(input())

CT = (M**e)%n
OT = (CT**d)%n

Sign = (M**d)%n
Verif = (Sign**e)%n

print ("CypherText ", CT, '\n',
       "Open Text: ", OT, '\n',
       "Signature: ", Sign, '\n',
        "Verification: ", Verif)