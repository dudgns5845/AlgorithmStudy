# # x -> y로 가는 것
# def search(x,y):
#     #좌표가 map 범위를 벗어나면 종료
#     if(x > N or x < 1 or y > N or y < 1):
#         return
#     #0이면 경로가 없음, 아님 이미 방문한 곳이면 최단 경로 에러이므로 종료
#     if(street[x][y] == 0 or visit[y] == 1):
#         return
#     #1이면 경로가 있음
#     elif street[x][y] == 1 :
#         #목적지 인덱스 공간에 방문 기록 남기기
#         visit[y] += 1
        
#         for i in range(1,N+1):
#             search(y,i)


# # N:도시의 개수 M: 도로의 개수 K: 거리 정보 X: 출발 도시의 번호
# N, M, K, X = map(int, input().split(" "))

# street = []
# #방문한 노드 기록
# visit = []

# #결과를 만족한 노드 기록
# result = []

# #지도 생성
# for i in range(N+1):
#     street.append([])
#     visit.append(0)
#     for j in range(N+1):
#         street[i].append(0)

# #도로 정보 반영하기
# for i in range(M):
#     x,y = map(int,input().split())
#     street[x][y] = 1


# #지도 출력해보기
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(street[i][j], end = ' ')
#     print()

# #첫 시작 노드는 L, 최단경로 중 거리가 K로 가는 노드를 찾아야한다
# #첫시작
# now_x = X
# now_y = 1
# #탐색 시작
# search(now_x,now_y)

# for i in range(1,N+1):
#     if i == X:
#         continue
#     elif visit[i] == K:
#         result.append(i)

# if len(result) == 0:
#     print(-1)
# else:
#     print(result) 


# # x -> y
# def search(x,y):
    
#     # x->y의 경로가 없거나 y에 이미 방문
#     if(street[x][y] == 0 or visit[y] == 1):
#         return
#     else:

from collections import deque

n,m,k,x = map(int,input().split())

#경로 저장할 2차원 배열 생성 -> 앞으로 이렇게 하기
board = [[] for _ in range(n+1)]


#방문을 확인하는 리스트
visit = [-1]*(n+1)

#처음 시작 노드는 미리 0처리
visit[x] = 0

#결과를 저장해 줄 리스트
answer=[]

#덱 생성과 동시 시작 노드 넣어주기
#덱은 앞과 뒤 둘다 삽입 삭제가 가능하다
que = deque([x])

#que가 다 비면 종료
while que:

    #현재 노드를 빼준다
    now = que.popleft()

    for i in board[now]:
        #방문 안했을 떄
        if visit[i] == -1:
            #지금 방문한 노드가 몇번째로 방문한걸 알기 위해서
            visit[i] = visit[now]+1
            #방문한 노드는 que에 넣어주기
            que.append(i)

#종료되고 난 뒤 결과를 봐보자 
for idx, length in enumerate(visit):
    #최단 경로의 길이와 같다면 
    if length == k:
        print(idx)
        answer.append(idx)
        continue

#최단 경로가 하나도 없을 땐 -1 출력 
if len(answer) == 0:
    print(-1)



