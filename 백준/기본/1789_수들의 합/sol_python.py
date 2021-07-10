#문제 https://www.acmicpc.net/problem/1789

import sys

n = int(sys.stdin.readline())

def solution(n):
    answer = 1
    while True:
        if answer * (answer+1) // 2 <= n < (answer+1) * (answer+2) // 2:
            return answer
        answer += 1

print(solution(n))