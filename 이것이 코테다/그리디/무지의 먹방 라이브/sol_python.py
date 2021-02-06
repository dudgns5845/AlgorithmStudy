food_time = list(map(int,input().split())
k = int(input())

#sum(리스트명)을 하면 리스트 모든 원소의 총합을 구할 수 있다.
#먹는 시간의 총합을 넘어가는 k를 입력받으면 그냥 -1을 리턴하면 된다
time_max = sum(food_time)

if k > time_max:
    print(-1)
else:
    while count != k:
        if food_time [ i % len(food_time) ] == 0:
            continue
        else:
            food_time [ i % len(food_time) ] -= 1
