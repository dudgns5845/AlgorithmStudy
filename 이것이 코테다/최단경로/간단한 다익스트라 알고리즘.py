import sys

#인풋함수 치환
input = sys.stdin.readline
#무한을 의미하는 10억
INF = int(1e9)

#노드의 개수, 간선의 개수를 입력 받기
n,m = map(int,input().split())
#시작 노드 번호를 입력받기
start = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [ [] for i in range(n+1)]
#방문 체크하는 리스트 생성
visted = [False] * (n+1)
#최단 거리 테이블 생성 -> 처음은 모두 무한으로 초기화
distance = [INF]*(n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    #a->b 사이의 거리가 c라는 뜻
    a,b,c = map(int,input().split())
    graph[a].append((b,c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1,n+1):
        if distance[i] < min_value and not visted[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visted[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visted[now] = True

    #현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
        cost = distance[now] + j[1]
        #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[j[0]]:
            distance[j[0]] = cost

#알고리즘 실행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
    #도달 할 수 없는 경우도 있다. 이때는 INF를 출력
    if distance[i] == INF:
        print("경로가 없습니다.")
    else:
        print(distance[i])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2