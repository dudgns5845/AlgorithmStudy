#문제 https://www.acmicpc.net/problem/1463

x = int(input())

dp = [0 for _ in range(x+1)]

count = 0

for i in range (2,x+1):
    
    #3단계 점화식 dp[i] = min(dp[i-1],dp[i//2],dp[i//3])+1
    dp[i] = dp[i-1]+1

    if i % 3 == 0:
        if dp[i] > dp[i//3] + 1:
            dp[i] = dp[i//3]+1
    if i % 2 == 0:
        if dp[i] > dp[i//2] + 1:
            dp[i] = dp[i//2] + 1

print(dp[x])
