#무슨 말인지 모르겠음.. 이건 수학적 쎈스가 있어야하는거 아닌가...
n = int(input())
coin_list = list(map(int,input().split()))

coin_list.sort()

result = 1

for i in coin_list:
    if result >= i:
        result += i
    else:
        break

print(result)


