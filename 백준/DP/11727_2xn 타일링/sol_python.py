#문제 https://www.acmicpc.net/problem/11727

n = int(input())

dp = [0] * (10000000)
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    if n == 1:
        print(dp[1])
        break
    if n == 2:
        print(dp[2])
        break
    else:
        dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n]% 10007)