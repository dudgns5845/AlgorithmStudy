#문제 https://www.acmicpc.net/problem/2294

import sys

n,k = map(int,sys.stdin.readline().split())

coins = [ int(input()) for _ in range(n)] 

dp = [ 0 for _ in range(k+1) ]


for i in range(1,k+1):
    answer = []
    for j in coins:
        if j <= i and dp[i-j] != -1:
           answer.append(dp[i-j])
    if not answer:
            dp[i] = -1
    else:
        dp[i] = min(answer) + 1

print(dp[k])            