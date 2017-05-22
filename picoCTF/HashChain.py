import md5 #Must be run in python 2.7.x

#code used to calculate successive hashes in a hashchain. 
seed = "1418"

#this will find the 5th hash in the hashchain. This would be the correct response if prompted with the 6th hash in the hashchain


hashc = seed
#print(md5.new("a").hexdigest())
while not hashc == "caca93dd9f20fbe0e4807e5b9ff6871b":
    hashc = md5.new(hashc).hexdigest()
    print(hashc)
