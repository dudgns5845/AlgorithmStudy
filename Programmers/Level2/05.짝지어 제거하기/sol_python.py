#문제 https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = 0

    stack = []

    for c in s:
        #스택에 하나씩 집어넣고 같으면 제거하고 다르면 지운다
        if len(stack) == 0:
            stack.append(c)
        #맨 마지막에 들어온 요소가 새로들어올 요소와 같는지 비교해서 같으면 스택제거
        elif stack[-1] == c:
            stack.pop()
        #같지 않으면 삽입
        else:
            stack.append(c)
    
    if len(stack) == 0:
        answer = 1

    return answer

s = "cdcd"
print(solution(s))