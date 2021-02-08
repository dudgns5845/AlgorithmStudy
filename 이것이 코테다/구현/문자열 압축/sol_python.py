input_string = input()
result_list = []

answer = 0

if len(input_string) == 1:
    answer = 1    

for token_length in range(len(input_string)//2,0,-1):
    #토큰의 개수
    count = 1

    #비교가 될 문자열을 추출하기
    token = input_string[0:i]

    #문자열 비교하기
    for i in range(0,len(input_string),len(test_string)):
        if i + len(test_string):
            break
        else:
            temp_string = input_string[i:i+len(test_string)]