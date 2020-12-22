def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
            
    #이런식으로 중복을 제거하면 정렬이 되지 않는다.        
    answer = list(set(answer))
    
    #정렬 메소드 sorted()s
    return sorted(answer)