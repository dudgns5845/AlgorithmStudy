def solution(n):
    answer = 0
    dp = [0,1,2,3,5]
    for i in range(5,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n] % 1234567