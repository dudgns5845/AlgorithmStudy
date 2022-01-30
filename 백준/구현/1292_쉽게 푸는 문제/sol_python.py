#문제 https://www.acmicpc.net/problem/1292

number_list = []
for i in range(1, 46):
    number_list += [i] * i
    
A, B = map(int, input().split())
print(sum(number_list[A-1:B]))