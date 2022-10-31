from collections import deque

def solution(n, edge):
    answer = 0
    
    # 노드 연결 관계 기록
    board = {}
    for i in range(n+1):
        board[i] = []
        
    # 노드 방문 여부 기록
    visited = [False] * (n+1)
    # 1로부터 해당 노드까지의 길이를 저장
    node_depth = [0]*(n+1)
    
    for x,y in edge:
        board[x].append(y)
        board[y].append(x)
    
    que = deque()
    que.append(1)
    visited[1] = True
    
    while que:
        
        start_node = que.popleft()
        
        for next_node in board[start_node]:
            if visited[next_node] == False:
                visited[next_node] = True
                node_depth[next_node] = node_depth[start_node]+1
                que.append(next_node)
    
    answer = node_depth.count(max(node_depth))
    
    return answer