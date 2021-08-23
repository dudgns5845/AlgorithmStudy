import sys

def solution(new_id):

    answer = ''
    new_id = new_id.lower()
    check_2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','_','-','0','1','2','3','4','5','6','7','8','9']
    
    for i in new_id:
        if i in check_2: #if i.isalnum() or i in '-_.':
            answer+= i

    while '..' in answer:
        anwer = answer.replace('..','.')

    answer = answer[1:] if answer [0] =='.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    answer = 'a' if answer == '' else answer        
            
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 3:
        answer += answer[-1]*(3-len(answer))
    
    return answer

temp = sys.stdin.readline()

solution(temp)


def solution(new_id):
    #1단계 & 2단계 소문자 치환, 제거
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())
    #3단계 . 2번 이상을 1개로 압축
    answer = re.sub('\.\.+','.',answer)
    #4단계 양끝 . 제거
    answer = answer.strip('.')
    #5단계 빈문자열 a 추가
    if answer =='': answer='a'
    #6단계 15개제외하고 문자모두제거, 우측 . 제거
    answer = answer[:15].rstrip('.')
    #7단계 길이 3 될 때까지 끝 문자 추가
    answer+=answer[-1]*(3-len(answer))
    return answer
