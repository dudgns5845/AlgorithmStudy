# from collections import deque

# def solution(progresses, speeds):
#     answer = []

#     temp = []

#     # for i,x in enumerate(zip(progresses,speeds)):
#     #     temp.append((i,x))
    
#     for i,x in enumerate(zip(progresses,speeds)):
#         temp.append([i,list(x)])
    
#     que = deque(temp)

#     while que:
        
#         first = que.popleft()
#         day = 0
#         count = 1
        
#         while first[1][0] < 100:
#             day += 1
#             first[1][0] += first[1][1]
        
#         #print(que)
        
#         for x in que:
#             x[1][0] = x[1][1] * day
#             if x[1][0] >= 100:
#                 print(x[0])
#                 #que.remove(x[0])
#                 count += 1
        
#         answer.append(count)
                
#     return answer


# list_1 = [95, 90, 99, 99, 80, 99]
# list_2 = [1, 1, 1, 1, 1, 1]	

# print(solution(list_1,list_2))

#문제 https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []
    
    left_day = []
    
    for i,j in zip(progresses, speeds):
        day = 0
        while i < 100:
            i += j
            day+=1
        left_day.append(day)

    que = deque(left_day)

    while que:
        count = 1
        first = que.popleft()
        while que:
            second = que.popleft()
            print(first,second)
            #다음 것이 같거나 작으면 실행
            if first >= second:
                count+=1
            #크면 다시 집어넣는다
            else:
                que.appendleft(second)
                break
        answer.append(count)


    return answer


list_1 = [95, 90, 99, 99, 80, 99]
list_2 = [1, 1, 1, 1, 1, 1]	

print(solution(list_1,list_2))