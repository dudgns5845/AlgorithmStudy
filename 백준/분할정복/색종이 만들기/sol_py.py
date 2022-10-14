import sys

N = int(sys.stdin.readline())

board = [list(map(sys.stdin.readlin().split())) for _ in range(N)]

blue = 0
white = 0

def solution(x,y,N):
    global blue, white
    color = board[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            # 같은 색이 아니면 재귀 호출
            if color != board[i][j]:
                solution(x,y,N/2)
                solution(x,y+N/2,N/2)
                solution(x+N/2,y,N/2)
                solution(x+N/2,y+N/2,N/2)
                
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1

solution(0,0,N)

print(white)
print(blue)


    