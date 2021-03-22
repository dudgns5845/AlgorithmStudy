n,m,k,x = map(int,input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

#노드간 연결관계를 입력받기
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1





#test case
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4