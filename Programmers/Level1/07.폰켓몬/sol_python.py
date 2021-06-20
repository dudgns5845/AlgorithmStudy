def solution(nums):
    answer = 0
    
    #가질 수 있는 포켓몬의 수
    total_count = len(nums)//2
    
    answer = total_count
    
    nums = list(set(nums))
    
    if total_count > len(nums):
        answer = len(nums)
    
    return answer