#열쇠 맞추기
def attach(x,y,M,key,board):
    for i in range(M):
        for j in range(M):
            #키와 둘이 더했을때 보드의 모든 값이 1이 되면 풀린 것
            board[x+i][y+j] += key[i][j]

#열쇠 빼기
def detach(x,y,M,key,board):
    for i in range(M):
        for j in range(M):
            #맞지 않으면 원래대로 보드의 값을 초기화 해줘야하므로
            board[x+i][y+i] -= key[i][j]

#키를 90도씩 회전해서 다 끼워 넣어보기
def rotate90(arr):
    #zip() 함수
    return list(zip(*arr[::-1]))

#열쇠가 맞는지 확인하기 
def check(board,M,N):
    for i in range(N):
        for j in range(N):
            #1이 아닌 0또는 2이면 열쇠가 맞지 않는 것!!
            if board[M+i][M+j] != 1:
                return False
    return True


def solution(key, lock):

    M,N = len(key), len(lock)

    #테스트할 보드판 만들기, 크기는 문제를 보고 이해하기
    board = [ [0] * ( M * 2 + N ) for _ in range( M * 2 + N )]

    #좌물쇠 중앙에 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key

    #모든 방향
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        
        for x in range(1, M+N):
            for y in range(1,M+N):
                #열쇠 넣어보기
                attach(x,y,M,rotated_key, board)

                #열쇠 풀렸는지 점검
                if(check(board,M,N)):
                    return True
                
                #틀렸으면 다시 복구
                detach(x,y,M,rotated_key,board)

    return False