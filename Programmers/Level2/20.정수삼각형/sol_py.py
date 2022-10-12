def solution(triangle):
    answer = 0
    dp = triangle
    
    for i in range(len(triangle)-2,-1,-1):
        for j in range(0,len(triangle[i])):
            dp[i][j] = max(triangle[i+1][j],triangle[i+1][j+1])+triangle[i][j]
    
    return dp[0][0]