
files = open("input.txt","r")
lines = files.readlines()
ans =0
for line in lines:
    numbers = (line.split("x"))
    nos= list(map(int, numbers))
    nos.sort()
    perimeter = 2 * int((nos[0])) + 2 * int((nos[1]))
    volume = nos[0]* nos[1] *nos[2]
    ans +=(volume+perimeter)
print(ans)