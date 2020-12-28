#파이썬은 math라이브러리에 gcd메소드가 구현되어있다...
from math import gcd

def solution(w,h):
    return w*h - (w+h -gcd(w,h))
