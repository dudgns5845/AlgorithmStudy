N = int(input())
fear = list(map(int,input().split()))
count = 0
#일반적으로 sort()는 오름차순
#sort(reverse=True)는 역정렬, 내림차순
fear.sort(reverse=True)

# 그룹을 최대로 만들어야 하므로

for i in range(len(fear)):
    if(N - fear[i] < 0):
        break
    else:
        count+=1
        N -= fear[i]
        i += fear[i] -1

print(count)