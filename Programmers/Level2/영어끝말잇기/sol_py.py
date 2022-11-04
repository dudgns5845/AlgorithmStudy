def solution(n, words):
    answer = [0,0]

    players = [[i,0] for i in range(1,n+1)]
    used = []
    idx = 0
    for word in words:
        idx %= n
        players[idx][1] += 1
        # 이미 말한 단어
        if word in used:
            answer = players[idx]
            return answer
        
        # 이전 말에 연결이 안된 상황
        if used: # 첫단어가 아니라면
            if used[-1][-1] != word[0]:
                answer = players[idx]
                return answer
        idx+=1
        used.append(word)
    
    return answer