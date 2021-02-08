from queue import PriorityQueue

def solution(food_times, k):
    answer = 0
    
    #우선 순위 큐를 생성
    que = PriorityQueue()

    #딕셔너리 타입으로 재정의
    for i in len(food_times):
        que.put((food_times[i],i+1))
    
    #음식 시간의 총합
    food_total_sum = sum(food_times)
    
    #k보다 음식의 시간이 작으면 -1 반환
    if food_total_sum <= k:
        return -1
    
    else:
        while True:
            shortest_time = que.get()[0]

            #가장 짧은 음식시간의 사이클을 돌 수 있는지 확인
            if k > shortest_time*len(food_times):
                #시간을 줄여주고
                k -= shortest_time*len(food_times)

            #돌은만큼 빼주기
            for i in que:
                que[i][0] -= shortest_time
            
            if shortest_time > k:
                break
    
    
    

    return answer