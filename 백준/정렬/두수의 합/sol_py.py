n = int(input())
arr = list(map(int,input().split(" ")))
x = int(input())
arr.sort()

count = 0

lt, rt = 0, n-1

while lt != rt:
    if arr[lt] + arr[rt] == x:
        count+=1
        lt += 1
    elif arr[lt] + arr[rt] > x:
        rt-=1
    else:
        lt+=1


print(count)