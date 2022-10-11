def solution(s):
    
    temp = []
    for spell in s:
        if spell == '(':
            temp.append(spell)
        else:
            if len(temp) == 0:
                 return False
            else:
                if temp[-1] == '(':
                    temp.pop()
    
    if len(temp) == 0:
        return True
    else:
        return False
        
    return True