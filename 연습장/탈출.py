from collections import deque


def Soution(maps):

    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in maps:
        for j in i:
            print(j,end= ' ')
        print()

    que = deque([(0,0)])
    visited[0][0] = 1

    while que:
        x,y = que.popleft()

        if x == n-1 and y == m-1:

            print("탈출 성공!!")
            print()
            for i in visited:
                for j in i:
                    print(j,end= ' ')
                print()
            
            return 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m:
                if visited[nx][ny] == 0:
                    if maps[nx][ny] == 1:
                        visited[nx][ny] = 1
                        que.append((nx,ny))
    
    print("탈출 실패")
    return
        

maps = [[1,1,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,1,1,1],[0,0,0,0,1]]

Soution(maps)