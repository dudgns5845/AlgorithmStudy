# import sys
# from collections import deque

# #좌표이동을 위한 조합 - 상하좌우
# d = [(-1,0),(1,0),(0,-1),(0.1)]

# #확산 함수
# def spread(candidate):
    
#     global n
#     for i in range(1,len(candidate)):
#         for j in range(1,len(candidate[i])):
#             r,c = candidate[i].popleft()
#             #동서남북 좌표 이동하면서 탐색 시작
#             for idx in range(4):
#                 nr = r + d[idx][0]
#                 if 0 <= nr and nr< n and 0<=nc and nc<n:
#                     board[nr][nc] = i
#                     candidate[i].append((nr,nc))
            

# #바이러스 종류 개수 받기
# n,k = map(int,input().split())

# #초기 상황 입력 받기 - 입력 받는게 중요!!
# board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# #덱을 사용할건데 굳이 바이러스의 최대를 알 필요가 있나...?
# s,x,y = map(int, input().split())

# #탐색 후보지를 넣을 덱 리스트 생성 -> 1번 2번 ... k번 별 덱 리스트드를 일일히 생성
# candidate = [deque([]) for _ in range(k+1)]

# for r in range(n):
#     for c in range(n):
#         if board[r][c]:
#             candidate[board[r][c]].append((r,c))

# time = 0

# while time < s:
#     spread(candidate)
#     time += 1

# print(board[x-1][y-1])




import sys

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread(n):
    global N
    virus = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == n:
                virus.append((i, j))

    while virus:
        r, c = virus.pop()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < N and 0 <= nc < N:
                if not matrix[nr][nc]:
                    matrix[nr][nc] = n

N, K = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())

time = 0

while time < S:
    for i in range(1, K+1):
        spread(i)
    time += 1

print(matrix[X-1][Y-1])