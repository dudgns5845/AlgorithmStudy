def solution(left, right):
    answer = 0

    for i in range(left,right+1):

        temp = 0

        for j in range(1, i+1):
            if i % j == 0:
                temp += 1

        print(temp)

        if temp % 2 == 0:
            answer += j
        else:
            answer -= j

    return answer

# 다른 사람 풀이
# 약수가 홀수인 경우는 제곱수인 경우이다
# 따라서 제곱근이 있는 경우를 채크해준다
# 방법은 if int(i**0.5)==i**0.5