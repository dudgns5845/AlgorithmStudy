def solution(n):
    ans = 0
    
    while n != 0:
        if n == 1:
            ans +=1
            break
        if n % 2 != 0:
            ans += 1
            n = n // 2
        else:
            n = n //2
    
    return ans