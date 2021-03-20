T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):
   
    if x < 0 and x >= m and y<0 and y>=n:
        return False

    # 방문하지 않았으면 일단 이 조건문을 실행하고 다른 곳을 방문하기도하고 결국엔 True를 반환
    if board[x][y] == 1:
        #해당 노드 방문 처리
        board[x][y] = 0

        #재귀적으로 호출
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            DFS(new_x,new_y)
            return True

    return False

for _ in range(T):
    m, n, k = map(int,input().split())

    #배추밭 생성
    board = [ [0] * n for _ in range(m) ]

    #배추 위치 받기
    for _ in range(k):
        x,y = map(int, input().split())
        board[x][y] = 1

    print("\n판 출력")
    for j in board:
        print(*j)

    #탐색 실시
    count = 0

    for i in range(m):
        for j in range(n):
            if DFS(i,j) == True:
                count += 1

    print("\n판 출력")
    for j in board:
        print(*j)

    print("-----------------")
    print(count)


#java 스크립트는 프론트 백엔드 앱에서 모두 사용된다 

"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""
