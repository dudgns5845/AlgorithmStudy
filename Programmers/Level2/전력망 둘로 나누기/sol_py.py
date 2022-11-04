from collections import defaultdict, deque

def BFS(n, startNode, arr, check):
    cnt = 1
    que = deque([startNode])
    visited = [True for _ in range(n+1)]
    visited[startNode] = False

    while que:
        node = que.popleft()
        for target in arr[node]:
            if check[node][target] and check[target][node] and visited[target]:
                visited[target] = False
                que.append(target)
                cnt += 1

    return cnt

def solution(n, wires):
    answer = n
    arr = defaultdict(list)
    check = [[False for _ in range(n+1)] for _ in range(n+1)]

    for x,y in wires:
        arr[x].append(y)
        arr[y].append(x)
        check[x][y] = True
        check[y][x] = True

    for a,b in wires:
        check[a][b] = False
        check[b][a] = False
        answer = min(answer, abs(BFS(n, a, arr, check) - BFS(n, b, arr, check)))
        check[a][b] = True
        check[b][a] = True

    return answer