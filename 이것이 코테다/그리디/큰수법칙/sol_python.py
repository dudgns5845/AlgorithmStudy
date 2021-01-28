#N,M,K 입력 받기
N,M,K = map(int,input().split())
#배열 입력 받기
ary = list(map(int,input().split()))

result = 0

ary.sort()

Max = input[:-1]
Second = input[:-2]

#M은 최종 연산 하는 횟수
while True:
    #최대값을 k번 더해주는 연산 실시
    for i in range(k):
        if M == 0:
            break
        result += Max
        m -= 1 #같은 수를 저장하는 데는 횟수 제한이 있다.

    if M == 0:
        break
    
    result += Second
    M -= 1

print(result)