def solution(s): 

    #압축된 문자열 길이 리스트
    length = []
 
    #압축된 결과 저장하는 곳
    result = ""
    
    #문자열이 1이면 그냥 압축 ㄴㄴ
    if len(s) == 1:
        return 1
    
    # 문자열을 인덱스 1부터 /2 까지 하기
    for term in range(1, len(s) // 2 + 1):
        
        #같은 문자열이 몇개인지 카운드 
        count = 1
        
        #점검할 문자열 추출
        temp_string = s[:term]

        #추출한 문자열과 비교
        for i in range (term, len(s), term):
            
            #문자열이 같으면 카운트
            if s[i:i+term] == temp_string:
                count += 1
            
            #문자열이 다른게 나타난 경우
            else:
                #같은게 한개도 없을 경우
                if count == 1:
                    count = "" #공란으로 만들어주고
                #count와 추출문자열을 저장해줌
                result += str(count) + temp_string

                #그리고 새로운 테스트 문자열로 변경
                temp_string = s[i:i+term]
                count = 1

        if count == 1:
            count = ""
        
        result += str(count) + temp_string
        #루프 한번 돌면 그 문자열 길이를 저장해줌
        length.append(len(result))
        
        #다시 초기화
        result = ""
    
    return min(length)
