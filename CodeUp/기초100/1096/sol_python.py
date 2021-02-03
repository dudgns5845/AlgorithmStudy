#python은 배열을 미리 할당하는게 개귀찬...
board= list()

#파이썬은 이차원 배열 
for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

size = int(input())

for i in range(size):
    x,y = map(int,input().split(" "))
    board[x][y] = 1


for i in range(1,20):
    for j in range(1,20):
        print(board[i][j],end = ' ')
    print() 