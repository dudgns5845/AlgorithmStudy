n = int(input())
board = [[0]*n for _ in range(n)]

#채워나갈 값 1씩 증가 최종값은 n*n
value = 1
row = 0
col = -1
inc = 1 #인덱스의 증감걍을 나타냄 1 or -1을 가짐

temp = n

while n > 0:
    for i in range(n):
        col += inc
        board[row][col] = value
        value+=1

    #전진하는 양 감소
    n-=1

    if n == 0: 
        break
    
    for i in range(n):
        row += inc
        board[row][col] = value
        value += 1
    
    inc *= -1 #부호를 변경시킨다

answer = 0 
for i in range(temp):
    print(board[i][i])
    answer += board[i][i]
