import heapq

def solution(scoville, K):
    answer = 0

    #list를 heapq로 변환
    heapq.heapify(scoville)

    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
            answer+=1
        else:
            return -1
    return answer