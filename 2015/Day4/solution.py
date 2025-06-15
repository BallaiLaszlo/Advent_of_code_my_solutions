import hashlib
number=0
input = "yzbqklnj"
md5_hash = hashlib.md5()
while True:
    input_string=input+str(number)
    md5_hash = hashlib.md5(input_string.encode('utf-8'))
    hash_result = md5_hash.hexdigest()
    #if hash_result[:5] == "00000": part 1
    if hash_result[:6] == "000000": # part 2
        print(hash_result)
        print(number)
        break
    number+=1
#part 1 : starts with 5 zeroes
#part 2 : starts with 6 zeroes