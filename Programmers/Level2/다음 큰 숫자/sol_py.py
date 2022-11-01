# python에는 숫자를 2진법 형태의 문자열로 반환해주는 메소드가 있다
# bin() => 0b******형태의 문자열이 반환된다.
# b = "01001111"
# x = int(b, 2) 2진 문자열을 정수로 바꾸는 방법
def solution(n):
     # 1의 개수 구하기
    n_cnt = bin(n).count('1')

    while n_cnt != bin(n+1).count('1'):
        n += 1
    return n+1