from collections import deque
import sys
input = sys.stdin.readline

N , M = map(int, input().split())

# 지도
board = [[0]*(N+1) for _ in range(N+1)]

# 방문 기록
visited = [False] * (N+1)

# 큐리스트
que = deque()

# 간선 등록
for _ in range(M):
    x,y = map(int, input().split())
    board[x][y] = board[y][x] = 1

def bfs(v,visited,board):
    # 방문 표시
    visited[v] = True
    que.append(v)

    while que:
        node = que.popleft()
        for i in range(1,N+1):
            if board[node][i] == 1 and visited[i] == False:
                visited[i] = True
                que.append(i)
                
            
count = 0
# 탐색 시작
for v in range(1,N+1):
    if visited[v] == False:
        bfs(v,visited,board)
        count += 1
    
print(count)