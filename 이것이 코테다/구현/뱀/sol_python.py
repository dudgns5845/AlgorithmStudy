N = int(input())
K = int(input())

board = []

for i in range(N+1):
    board.append([])
    for j in range(N+1):
        board[i].append(0)

for i in range(K):
    x,y = map(int,input().split(" "))
    #사과 셋팅
    board[x][y] = 1

L = int(input())

for i in range(L):





