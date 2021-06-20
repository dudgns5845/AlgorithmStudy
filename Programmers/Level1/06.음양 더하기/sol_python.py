#문제
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]  == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


    #다른 유저 풀이
    #zip(list_1, list_2)를 하면 
    #(1,1) (2,2) 이런식으로 반환해준다
    #for i in zip(list,list)