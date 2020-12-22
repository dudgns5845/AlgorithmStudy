def solution(participant, completion):
    answer = ''

    #파이썬에는 list를 정렬하는 메소드가 다양하다.
    #sorted(List) or List.sorted()
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if(completion[i] != participant[i]):
            return participant[i]
    
    #List[-1]은 맨 마지막 요소 반환
    return participant[-1]