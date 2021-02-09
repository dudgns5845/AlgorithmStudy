#dfs함수
def DFS(start):
    #시작 노드는 미리 방문 처리
    visit_dfs[start] = 1

    print(start, end=' ')
    
    #노드 개수만큼 반복문 실시
    for i in range(1,n+1):
        #방문하지 않았고 연결 상태일 때 재귀 호출
        if visit_dfs[i] == -1 and board[start][i] == 1:
            DFS(i)

#bfs함수
def BFS(start):

    #bfs는 경로를 따로 저장해줘야한다
    queue = [start]
    
    #방문 기록 처리
    visit_bfs[start] = 1

    #queue가 아무것도 없을때까지 반복
    while queue:
        start = queue.pop(0)
        print(start,end=' ')

        for i in range(1,n+1):
            if visit_bfs[i] == -1 and board[start][i] == 1:
                queue.append(i)
                visit_bfs[i] = 1

#map 정보 입력 받기
n, m, v = map(int,input().split())

#입력 받은 정보로 map 생성하기
board = [[0]*(n+1) for _ in range(n+1)]

#간선 입력하기
for i in range(m):
    x,y = map(int,input().split())
    board[x][y] = board[y][x] = 1

#방문 기록 리스트
visit_dfs = [-1] * (n+1)
visit_bfs = [-1] * (n+1)

#지도 출력해보기
for i in range(1,n+1):
    for j in range(1,n+1):
        print(board[i][j],end=' ')
    print()


DFS(v)
print()
BFS(v)
print()

print(visit_dfs)
print(visit_bfs)