import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split(" ")))
M = int(input())
B = list(map(int,sys.stdin.readline().split(" ")))
A.sort()

for i in B:
    start = 0
    end = N - 1
    result = False
    while start <= end:
        mid = (start + end)//2
        if A[mid] == i:
            result = True
            break
        elif A[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    if result == True:
        print(1)
    else:
        print(0)
