#문제 https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):

    answer = 0
    
    # 지도 사이즈 및 도착 위치 , 목적지는 -1 해야함
    n = len(maps)
    m = len(maps[0])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]



    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1



    que = deque([(0,0)])
    
    # 경로 길이 카운트
    count = 0

    while que:
        x,y = que.popleft()
        
        #목적지 도착시 종료!
        if x == n-1 and y == m -1:
            return visited[n-1][m-1]
        
        for i in range(4):
             nx , ny = x + dx[i] , y + dy[i]
             if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx,ny)) 
        

    for i in visited:
        for j in i:
            print(j ,end =' ')
        print() 


    return -1


# 테스트 케이스
temp = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]

print(solution(temp))



# 맵 출력해보기
for i in temp:
    for j in i:
        print(j, end = ' ')
    print()

