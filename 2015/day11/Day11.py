def checkInc(password):
    password = list(password)
    for i in range(len(password)-2):
        if ord(password[i])+1==ord(password[i+1]) and ord(password[i+1])+1==ord(password[i+2]):
            return True
    return False

def twoOverLapping(password):
    i =0
    pair = set()
    while i<len(password)-1:
        if password[i] == password[i+1]:
            pair.add(password[i])
            i+=2
        else:
            i+=1
    return len(pair)>=2

def checkLetters(password):
    if any(i in password for i in "iol"):
        return False
    return True

def is_valid_password(password):
    if(checkInc(password) and checkLetters(password) and twoOverLapping(password)):
        return True
    else:
        return False

def incrementPassword(password):
    password = list(password)
    i = len(password)-1
    while i>=0:
        if password[i]=='z':
            password[i]='a'
            i-=1
        else:
            password[i] = chr(ord(password[i])+1)
            break

    return ''.join(password)

def find_next_password(password):
    password = incrementPassword(password)
    while not is_valid_password(password):
        password = incrementPassword(password)
    return password

if __name__ == '__main__':
    print(find_next_password("vzbxkghb"))
    print(find_next_password("vzbxxyzz"))




