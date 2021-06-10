# 타일을 몇개를 사용 가능한지 물어보는 것


n = int(input())

#bottom up solution

dp = [0]*1000

#이건 초기 셋팅값
dp[1] = 1
dp[2] = 3
~
#타일문제 생각보다 쉬웠네....
for i in range(3,n+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[n])