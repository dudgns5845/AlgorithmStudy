#문제 https://www.acmicpc.net/problem/10844
import sys

#num의 자리수
num = int(sys.stdin.readline())

#num의 자리수 만큼 생성
dp = [[0]*10 for _ in range(num+1)]

#1의 자리를 셋팅해주면 다음 점화식이 가능
      #  0 1 2 3 4 5 6 7 8 9
dp[1] = [0,1,1,1,1,1,1,1,1,1]

#2자리부터는 점화식 적용
for i in range(2,num+1):
    #끝자리가 0일때
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

#결과 출력
print(sum(dp[num])%1000000000)

#dp 값들이 잘 처리 됐는지 출력해보기
for i in range(1,num+1):
    for j in range(10):
        print(dp[i][j], end = ' ')
    print()

