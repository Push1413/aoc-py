import re

files = open("input.txt","r")
lines = files.readlines()
reqPaper =0
for line in lines:
    numbers = re.findall(r'\d+', line)
    l, w, h = map(int, numbers)
    minSide = min(l*w,w*h, h*l)
    reqPaper += 2*l*w + 2*w*h + 2*h*l + minSide

print(reqPaper)


