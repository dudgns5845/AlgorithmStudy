import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))

    distance[start] = 0

    #que가 비어있으면 반복문 종료
    while q:
        #최단 거리 노드 꺼내기
        dist, now = heapq.heappop(q)

        #현재 노드가 이미 처리되어 있다면 무시하기 
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("경로가 없습니다.")

    else:
        print(distance[i])
