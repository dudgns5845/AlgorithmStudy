def solution(pos):
    answer = 0
    now_y = 66-ord(pos[0])
    now_x = int(pos[1])
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]
    
    for i in range(8):
        new_x = now_x + dx[i]
        new_y =  now_y + dy[i]
        print(new_x,new_y)
        if 0< new_x <= 8  and  0< new_y <= 8:
           
            answer+=1
    
    return answer

pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")