N = int(input())

dp=[0]*(N+1)


for i in range(2,N+1):

    #1을 빼는 케이스
    dp[i] = dp[i-1] + 1

    if N % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)

    if N % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[N])