n,m = map(int,input.split())

#최종 결과값을 저장
result = 0

for i in range(n):
    #한 라인씩 입력을 받는다.
    ary_line = list(map(int,input.split()))

    #min() ==> list의 요소 중에 최소값을 반환해준다
    min_value = min(ary_line)
    #각 라인들의 최소값들 중에 최대인 것을 찾는것이므로
    result = max(result,min_value)

print(result)