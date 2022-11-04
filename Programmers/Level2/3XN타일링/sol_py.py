def solution(n):
    answer = 0
    n %= 1000000007
    dp= [0,0,3,0,11]
    if n % 2 != 0: #n이 홀수
        return 0
    else: #n이 짝수
        for i in range(5,n+1):
            dp.append((4*dp[i-2]-dp[i-4])%1000000007)

    return dp[n]