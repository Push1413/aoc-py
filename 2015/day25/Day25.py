def getCode(r,c):
    index = ((r+c-1)* (r+c-2))/2 + c
    firstCode = 20151125
    i =1
    while i!=index:
        next_code = (firstCode * 252533) % 33554393
        i+=1
        firstCode = next_code
    print(next_code)

if __name__=='__main__':
    getCode(r=2978, c =3083)
