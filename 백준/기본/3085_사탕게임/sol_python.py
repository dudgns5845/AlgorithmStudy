#문제 https://www.acmicpc.net/problem/3085
import sys

def solution(board):

    #크기 가져오기
    n = len(board)

    #순회를 하면서 최고값이 나타나면 값을 갱신. 최종 반환 값
    answer = 1

    #순회
    for i in range(n):

        #임시 변수
        count = 1
        # 열 순회(가로)
        for j in range(1,n):
            #이전 값과 같으면 증가
            if board[i][j-1] == board[i][j]:
                count += 1
            #같지 않으면 다시 1로 초기화
            else:
                count = 1
            
            # 위 조건을 체크하고 나왔을때 값이 최종값보다 크면 최종값을 갱신
            if count > answer:
                answer = count

        # 행 순회(세로)
        count = 1
        for j in range(1,n):
            if board[j-1][i] == board[j][i]:
                count += 1
            else:
                count = 1
            if count > answer:
                answer = count

    return answer


n = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for _ in range(n)]

answer = 0

# 인접한 것 바꾸기 구현
for i in range(n):
    for j in range(n):
        if j + 1 < n :
            #좌우로 바꾸기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            #최대 개수 구하고 최댓값 받아오기
            temp = solution(board)

            #최댓값 갱신
            if answer < temp:
                answer= temp

            #원래대로 돌려놓기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i + 1 < n:
            #상하로 바꾸기
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            #최대 개수 구하고 최댓값 받아오기
            temp = solution(board)
             #최댓값 갱신
            if answer < temp:
                answer= temp
             #되돌려놓기
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)

