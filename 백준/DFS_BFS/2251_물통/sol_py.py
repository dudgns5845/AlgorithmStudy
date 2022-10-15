import sys
from collections import deque

# 입력처리
a,b,c = map(int,sys.stdin.readline().split())

# 큐리스트
q = deque()
q.append((0,0))

# 방문 여부
visited = [[False]*(b+1) for _ in range(a+1)]

visited[0][0] = True

# 결과값
answer = []

# x,y의 경우의 수를 저장
def pour(x,y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()
        z = c - x - y

        # A비커가 비어 있는 경우 저장
        if x == 0:
            answer.append(z)
        
        # A->B
        water = min(x,b-y)
        pour(x-water,y+water)

        # A->C
        water = min(x,c-z)
        pour(x-water,y)

        # B->A
        water = min(y,a-x)
        pour(x+water,y-water)

        # B->A
        water = min(y,c-z)
        pour(x,y-water)

        # C->A
        water = min(z,a-x)
        pour(x+water,y)

        # C->B
        water = min(z,b-y)
        pour(x,y+water)


#호출
bfs()

answer.sort()

for i in answer:
    print(i, end=" ")