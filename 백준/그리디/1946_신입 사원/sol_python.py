import sys
# 테스트 케이스
t = int(input())

for _ in range(t):

    #신규 회원 수 --> 나중에 출력해야함
    result = 1 

    #지원자 성적 담는 곳 
    volunteer = []

    #지원자 수
    n = int(input())
    for i in range(n):
        #x는 서류 등수 y는 면접 등수
        x,y = map(int,sys.stdin.readline().split())
        volunteer.append([x,y])

    #서류 기준 정렬   
    volunteer.sort()
    # print(volunteer)

    #면접 점수
    max = volunteer[0][1]

    for i in range(1,n):
        if max > volunteer[i][1]:
            result += 1
            max = volunteer[i][1]

    print(result)


       




