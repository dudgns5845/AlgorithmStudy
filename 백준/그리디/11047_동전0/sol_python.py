n, k = map(int,input().split())
coin_list = []
totalCoin_Count = 0
for i in range(0,n):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

for i in range(0,n):
    if coin_list[i] > k:
        continue
    temp = k//coin_list[i]
    k = k - temp*coin_list[i]
    totalCoin_Count += temp

print(totalCoin_Count)
