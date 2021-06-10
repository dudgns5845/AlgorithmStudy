# 문제 링크 https://www.acmicpc.net/problem/2178

from sys import stdin
from collections import deque
n,m = map(int,input().split())

#미로 입력 받기 
board = [stdin.readline().rstrip() for _ in range(n)]

#방문 기록
visted = [ [0] * m for _ in range(n) ]

#좌표 이동을 위한 셋팅
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    #시작은 0,0부터
    que = deque([(0,0)])
    visted[0][0] = 1

    while que:
        x , y = que.popleft()

        if x == n - 1 and y == m-1:
            print(visted[n-1][m-1])
            return
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            #새로 이동하려는 좌표가 지도 내부 좌표인지 체크하고
            if 0 <= new_x < n and 0 <= new_y < m:
                #그 좌표를 이미 방문했는지 체크하고
                if board[new_x][new_y] == '1' and visted[new_x][new_y] == 0:
                    visted[new_x][new_y] = visted[x][y] + 1
                    que.append((new_x,new_y))
                    
bfs()





        


