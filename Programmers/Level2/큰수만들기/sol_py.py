def solution(number, k):
    
    stack = []
    
    for num in number:
        while stack and k > 0 and num > stack[-1]:
            k -= 1
            stack.pop()
        stack.append(num)
    
    if k > 0:
        stack = stack[:-k]
    
    return "".join(stack)