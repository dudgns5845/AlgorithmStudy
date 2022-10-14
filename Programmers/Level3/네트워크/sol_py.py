def solution(n, computers):
    answer = 0

    visited = [False] * n

    # i,i 자신 간선 없앰
    for i in range(n):
        #방문 안했으면 진행
        if visited[i] == False:
            DFS(n,computers, i , visited)
            #연결된거 다 끝났으면 count증가
            answer += 1

    return answer
                

def DFS(n,computers, start, visited):
    #방문 처리해주고
    visited[start] = True

    #순회 시작
    for i in range(n):
        #연결 되어있으며
        if computers[start][i] == 1:
            #방문을 하지 않았을때
            if visited[i] == False:
                #재귀 시작
                DFS(n,computers,i,visited)