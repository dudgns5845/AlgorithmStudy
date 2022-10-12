def solution(m, n, puddles):
    board = [[0]*(m+1) for _ in range(n+1)]
        
    # 웅덩이 처리
    for i in puddles:
        board[i[1]][i[0]] = 0
    
    board[1][1] =1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1: 
                continue
            if [j,i] in puddles:
                continue
            else:
                board[i][j] = (board[i-1][j]+board[i][j-1] )% 1000000007
    
    return board[i][j]