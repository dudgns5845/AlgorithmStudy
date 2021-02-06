input_string = input()
count_0 = 0
count_1 = 0
result = 0

temp = input_string[0]
if temp == '0':
    count_0 += 1
else:
    count_1 += 1

for i in range(len(input_string)-1):
    
    temp = input_string[i]
    
    if temp != input_string[i+1]:
        if input_string[i+1] == '0':
            count_0 += 1
        else:
            count_1 += 1

result = min(count_1, count_0)

print(result)

    