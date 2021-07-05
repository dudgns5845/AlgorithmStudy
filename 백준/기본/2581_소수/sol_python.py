#문제 https://www.acmicpc.net/problem/2581
import sys
m,n = map(int,sys.stdin.readline().split())

prime = []

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if(num%i == 0):
            return False
    return True

for i in range(m,n+1):
    if isPrime(i):
        prime.append(i)

if not prime:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])