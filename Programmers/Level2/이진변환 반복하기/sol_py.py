def solution(s):
    # answer[0] 횟수 answer[1] 개수
    answer = [0,0]
    while True:
        print(s)
        answer[0] += 1
        answer[1] += s.count('0')
        s = bin(len(s)-s.count('0'))[2:]
        if s == "1":
            break
    return answer


solution("110010101001")
