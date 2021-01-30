n = int(input())
move_list = list(input().split())

#시작 위치는 (1,1)부터
x = 1
y = 1

for i in range(len(move_list)):
    if move_list[i] == 'R' and y+1 <= n:
        y+=1

    elif move_list[i] == 'L' and y-1 >= 1:
        y-=1

    elif move_list[i] == 'U' and x-1 >= 1:
        x-=1

    elif move_list[i] == 'D' and x+1 >= n:
        x+=1 

print(x, y)
    