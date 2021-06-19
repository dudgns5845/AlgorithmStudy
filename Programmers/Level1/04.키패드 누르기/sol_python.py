#절대값을 위한 라이브러리
import math

#파이썬에서 튜플, 딕셔너리 등 자료형 입력 및 접근법 잘 이해하기
board = {'1' : (0,0),'2' : (0,1), '3':(0,2), 
'4' : (1,0),'5' : (1,1), '6':(1,2),
'7' : (2,0),'8' : (2,1), '9':(2,2),
'*' : (3,0),'0' : (3,1), '#':(3,2)}

#원소 접근 및 출력해보기
for i in board:
    print(board[i][0],board[i][1])


def solution(numbers, hand):
    answer = ''
    
    #현재 손가락 좌표
    now_R = board['#']
    now_L = board['*']

    numbers = map(str, numbers)

    print(now_L,now_R)

    for i in numbers:
        #무조건 왼쪽
        if i in ['1','4','7']:
            answer += 'L'
            now_L = board[i]
        #무조건 오른쪽
        elif i in ['3','6','9']:
            answer += 'R'
            now_R = board[i]
        #2580일때 
        else:
            #여기가 관건, 원소 접근하기
            x,y = board[i][0],board[i][1]
            if abs(x - now_R[0]) + abs(y-now_R[1]) > abs(x - now_L[0]) + abs(y-now_L[1]):
                answer += 'L'
                now_L = board[i]
            elif abs(x - now_R[0]) + abs(y-now_R[1]) < abs(x - now_L[0]) + abs(y-now_L[1]):
                answer += 'R'
                now_R = board[i]
            else:
                if hand == 'left':
                    answer += 'L'
                    now_L = board[i]
                else:
                    answer += 'R'
                    now_R = board[i]

        #단계별 상황 출력해보기
        print(now_L,now_R,answer[-1])


    return answer

#테스트 케이스
tt = [2,5,8,0]	
th = 'right'

print(solution(tt,th)) 