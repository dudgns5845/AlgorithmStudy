# N = int(input())
# M = int(input())

# #1번 컴퓨터부터 시작
# start_node = 1

# #map 생성
# board = [ [0] * (N+1) for _ in range(N+1) ]
# #방문 체크 리스트 생성
# visit = [-1]*(N+1)

# for _ in range(M):
#     x,y = map(int,input().split())
#     board[x][y] = board[y][x] = 1

# def DFS(start):

#     visit[start] = 1

#     for i in range(1,N+1):
#         if board[start][i] == 1 and visit[i] == -1:
#             DFS(i)

# DFS(start_node)

# print(visit.count(1)-1)

    
#dfs로 풀어야할 꺼 같군!
n = int(input())
m = int(input())

board = [[0]*(n+1) for _ in range(m+1)]
visted = [False]*(n+1)

dfs_list = []

for i in range(m):
    x,y = map(int,input().split())
    board[x][y] = 1 

def dfs(start):

    visted[start] = True

    for i in range(1,n+1):
        if visted[i] == False:
            if board[start][i] == 1:
                dfs_list.append(i)
                dfs(i)

dfs(1)

print(len(dfs_list))







