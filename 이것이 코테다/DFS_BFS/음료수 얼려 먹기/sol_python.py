n, m = map(int, input().split())

board = []

for i in range(n):
    #연속으로 나열된 숫자를 이렇게 입력 받아도 되네...
    board.append(list(map(int,input())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):

    if x < 0 and x >= n and y<0 and y>=m:
        return False

    # 방문하지 않았으면 일단 이 조건문을 실행하고 다른 곳을 방문하기도하고 결국엔 True를 반환
    if board[x][y] == 0:
        #해당 노드 방문 처리
        board[x][y] = 1

        #재귀적으로 호출
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            DFS(new_x,new_y)
            return True
        
        #여기까지 왔다면 더이상 방문할 곳이 없다는 것
    
    # board[x][y] == 1 일 경우 즉 방문했던 곳이라는 말
    return False

#아이스크림 개수 저장
count = 0 

#메인문 
for i in range(n):
    for j in range(m):
        #해당 좌표에서 
        if DFS(i,j) == True:
            count += 1

print(count) 