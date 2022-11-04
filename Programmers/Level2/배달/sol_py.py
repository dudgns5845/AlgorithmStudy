# from collections import deque

# def solution(N, road, K):
#     answer = 0
#     access_node = []

#     board = [[0]*(N+1) for _ in range(N+1)]
#     visited = [False] * (N+1)
#     distance_node = [0] * (N+1)
    
#     for a,b,c in road:
#         if board[a][b] == 0:
#             board[a][b] = board[b][a] = c
#         else:
#             board[a][b] = board[b][a] = min(board[a][b],c)
    
#     que = deque()
#     que.append(1)
#     visited[1] = True
    
#     while que:
#         start = que.pop()
#         for idx,connect in enumerate(board[start]):
#             if connect != 0:
#                 if visited[idx] == False:
#                     distance_node[idx] = distance_node[start] + board[start][idx]
#                     if distance_node[idx] <= K:
#                         que.append(idx)
#                         access_node.append(idx)
#                         visited[idx]=True
#                     else:
#                         continue
#     return answer



#플로이드 와샬로 풀 것

# from collections import deque

# def solution(N, road, K):
#     INF = int(1e9)
#     # 그래프 표현
#     board = [[] for _ in range(N+1)]
   
#     for x,y,z in road:
#         # 같은 노드에 간선이 2개 이상 있을 수 있음
#         board[x].append((y,z))
#         board[y].append((x,z))
    

#     # 방문 기록
#     visited = [False] * (N+1)
#     # 최단 경로 기록
#     distance = [INF] * (N+1)

#     que = deque()

#     # 탐색 시작 시작 노드 1
#     visited[1] = True
#     distance[1] = 0
#     que.append(1)

#     while que:
#         start = que.popleft()

#         for i in range(1,N+1):
#             if visited[i] == False and 0 < board[start][i] < 123456789:
#                 distance[i] = min(board[start][i] + distance[start], distance[i])
        








# road= [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# solution(5,road,3)


import heapq

heap = []

heapq.heappush(heap,10)
heapq.heappush(heap,5)
heapq.heappush(heap,50)
heapq.heappush(heap,1)
print(heap)
heap.pop()
