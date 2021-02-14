from collections import deque

n, m = map(int,input().split())

board = []

queue = deque()

for i in range(n):
    board.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):

    #방문 가능한 노드 추가 -> 큐에 노드 추가
    queue.append((x,y)) 

    #큐가 빌때까지 반복 -> 큐를 실행
    while queue:
        x,y = queue.popleft()

        #상하좌우 탐색
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            #DFS와 반대로 BFS는 인덱스의 범위를 확인하고 
            #방문 가능한 노드인지 확인하고 재귀호출을한다
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                if board[new_x][new_y] == 1:
                    board[new_x][new_y] = board[x][y] + 1
                    queue.append((new_x,new_y))
    
    return board[n-1][m-1]

print(BFS(0,0))

for i in board:
    print(*i)

"""
5 6
101010
111111
000001
111111
111111
"""