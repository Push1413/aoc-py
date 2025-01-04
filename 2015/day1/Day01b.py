file = open("input.txt",'r')
line = file.readline()
count =0
index =0
for char in line:
    index+=1
    if char =='(':
        count+=1
    if char == ')':
        count-=1
    if count==-1:
        print(index)
        break

print(index)
