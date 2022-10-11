def solution(board):
    
    max_box = 0

    #좌우가 2보다 작을 직사각형을 고려할것
    if len(board) == 1 or len(board[0]) == 1:
        for word in board:
            if word.count(1) != 0:
                return 1
            else:
                return 0
                    
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j]==1:
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1])+1
                max_box = max(max_box,board[i][j])
    return max_box**2