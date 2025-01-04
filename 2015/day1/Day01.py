file = open("input.txt",'r')
lines = file.readlines()
count =0
for line in lines:
    for char in line:
        if char =='(':
            count+=1
        elif char == ')':
            count-=1

print(count)
