import sys

# 3차원 메모리 제이션 (a,b,c) 0 <= a,b,c <= 20
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):

    if a <= 0 or b<=0 or c<=0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    #메모리제이션 값이 있다면 값을 리턴
    if dp[a][b][c]:
        return dp[a][b][c]

    #값이 없을 경우 계산
    #경우 1
    if a < b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c] 
    #경우 2
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return dp[a][b][c]

while True:
    a, b,c = map(int,sys.stdin.readline().split())

    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')



