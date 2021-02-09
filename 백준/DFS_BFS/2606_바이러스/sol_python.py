N = int(input())
M = int(input())

#1번 컴퓨터부터 시작
start_node = 1

#map 생성
board = [ [0] * (N+1) for _ in range(N+1) ]
#방문 체크 리스트 생성
visit = [-1]*(N+1)

for _ in range(M):
    x,y = map(int,input().split())
    board[x][y] = board[y][x] = 1

def DFS(start):

    visit[start] = 1

    for i in range(1,N+1):
        if board[start][i] == 1 and visit[i] == -1:
            DFS(i)

DFS(start_node)

print(visit.count(1)-1)

    



