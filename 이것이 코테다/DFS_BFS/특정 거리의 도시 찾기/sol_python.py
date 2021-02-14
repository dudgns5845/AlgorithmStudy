import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x=map(int,input().split())
node=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    node[a].append(b)

dist=[-1]*(n+1)
dist[x]=0

q=deque([x])

while q:
    now=q.popleft()
    for i in node[now]:
        if dist[i] == -1:
            dist[i]=dist[now]+1
            q.append(i)

for idx,d in enumerate(dist):
    if d == k:
        print(idx)
        break
    else:
        print(-1)