from collections import deque

def solution(priorities, location):
    answer = 0

    #enumerate()는 0,원소1 / 1,원소2 / ...이런식으로 생성해준다
    que = deque([v,i] for i , v in enumerate(priorities))

    while len(que):
        # 일단 첫 원소 가져옴
        item = que.popleft()
        # 큐가 원소가 남아있고, 최대값보다 맨 처음 원소의 값이 작다면 뒤로 빠꾸
        if que and max(que)[0] > item[0]:
            que.append(item)

        #지금 popleft한게 맥스 값일때, 또는 맥스 값들이 다 없고 이제 같은 값들을 비교할때
        else:
            answer += 1
            # 아이템의 인덱스가 처음 위치 그 원소면 스탑 
            if item[1] == location:
                break