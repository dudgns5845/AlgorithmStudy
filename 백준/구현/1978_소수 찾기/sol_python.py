#문제 https://www.acmicpc.net/problem/1978
import sys

n = int(input())
temp = list(map(int,sys.stdin.readline().split()))
answer = 0

#에라토스테네스의 체
def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if(num%i == 0):
            return False
    return True

for i in temp:
    if isPrime(i):
        answer += 1

print(answer)