def solution(arr):
    answer = max(arr)
    while True:
        check = False
        for i in arr:
            if answer % i == 0:
                check = True
            else:
                check = False
                break
        if check == True:
            return answer
        answer += 1