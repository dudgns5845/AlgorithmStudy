#문제 https://programmers.co.kr/learn/courses/30/lessons/43165

#bfs로 풀기
def solution(numbers, target):
    answer = 0

    child = [0]

    for i in numbers:
        temp = []
        for j in child:
            temp.append(j+i)
            temp.append(j-i)
        
        child = temp
    # 위 반복문을 다 수행하면 child는 모든 가지의 값들을 가지고 있다
    for i in child:
        if i == target:
            answer += 1    
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers,target))