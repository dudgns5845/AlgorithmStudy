input_string = input()
char_ary = []
int_ary = []

for i in input_string:
    #문자열 비교 이렇게도 가능함
    if 'A' <= i and i <= 'Z':
        char_ary.append(i)
    else:
        int_ary.append(int(i))

char_ary.sort()
result = sum(int_ary)

#리스트의 내용을 하나의 문자열로 만드는법
#''.join(리스트명)
print(''.join(char_ary)+"%d"%result)
