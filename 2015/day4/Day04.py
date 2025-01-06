import hashlib

i=1
prefixStar=5
prefixStarPartB =6
j=254575
prefix = "bgvyzdsv"
while True:
    valueA = prefix + str(i)
    valueB = prefix + str(j)
    hash_result = hashlib.md5(valueA.encode()).hexdigest()
    hash_result_b = hashlib.md5(valueB.encode()).hexdigest()
    if hash_result[:prefixStar]=="00000":
        print(i)
    if hash_result_b[:prefixStarPartB]=="000000":
        print(j)
        break
    i+=1
    j+=1

