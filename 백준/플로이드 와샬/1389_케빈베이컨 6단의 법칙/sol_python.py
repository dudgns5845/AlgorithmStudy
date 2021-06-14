#문제 https://www.acmicpc.net/problem/1389
import sys
n,m = map(int, sys.stdin.readline().split())
inf = 10000000
#연결관계 저장

board = [[inf]*(n+1) for _ in range(n+1)]
result = []

#연결 관계 입력 받기
for i in range(m):
    x,y = map(int,input().split())
    board[x][y] = 1
    board[y][x] = 1

# 자기 노드로 가는 것은 0으로 초기화
for i in range(1,n+1):
    board[i][i] = 0

def floydWarshall():
    #거쳐가는 노드
    for k in range(1,n+1):
        #출발노드
        for i in range(1,n+1):
            #도착노드
            for j in range(1,n+1):
                if board[i][k] + board[k][j] < board[i][j]:
                    board[i][j] = board[i][k] + board[k][j]
floydWarshall()

for i in range(1,n+1):
    result.append(sum(board[i])-inf)

# 결과값들 출력
# print(result)


# 탐색 종료후 결과 확인해보기
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(board[i][j],end=' ')
#     print()

#최소값의 인덱스 반환하기
print(result.index(min(result))+1)


