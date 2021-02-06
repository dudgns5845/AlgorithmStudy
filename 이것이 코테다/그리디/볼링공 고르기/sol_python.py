n,m = map(int,input().split())
weight_list = list(map(int,input().split()))
count = 0
for i in range(n-1):
    for j in range(i+1,n):
        if(weight_list[i] == weight_list[j]):
            continue
        count += 1

print(count)



