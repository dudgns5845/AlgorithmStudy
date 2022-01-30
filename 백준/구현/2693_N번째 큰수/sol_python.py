#문제 https://www.acmicpc.net/problem/2693
import sys

test = int(input())

for _ in range(test):
    temp = list(map(int, sys.stdin.readline().split()))
    temp.sort()
    print(temp[-3])


