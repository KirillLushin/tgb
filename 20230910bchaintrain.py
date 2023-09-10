import urllib.request
import json

count = 0
miners = []
for i in range(0, 20):
    url = f"https://blockchain.info/block-height/{34}?format=json"
    r = urllib.request.urlopen(url)
    data = json.load(r)
    sp = data['blocks'][0]['tx'][0]['out'][0]['spent']
    addr = data['blocks'][0]['tx'][0]['out'][0]['addr']
    if sp == False:
        count += 1
        miners.append(addr)
print (count)
print(miners)


