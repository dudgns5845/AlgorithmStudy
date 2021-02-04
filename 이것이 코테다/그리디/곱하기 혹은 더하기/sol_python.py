#공백이 없는 숫자문자열을 하나씩 쪼개는 것이 관건인듯
num_string = input()
ary = []
result = 0

for i in range(len(num_string)):
    ary.append(int(num_string[i]))

for i in ary:
    print(i)
    if(i == 0):
        continue
    elif result == 0:
        result += i
    else:
        result *= i

print(result)