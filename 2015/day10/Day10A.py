input = "1321131112"

for i in range(40):
    output=""
    left =0
    right = 1
    while right < len(input):
        if input[right] ==input[left]:
            right+=1
        else:
            output+=str(right-left)
            output+=input[left]
            left=right

    output += str(right - left)  # Count of the last group
    output += input[left]
    input = output

print(len(output))




