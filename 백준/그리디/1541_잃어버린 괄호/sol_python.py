# 문제 https://www.acmicpc.net/problem/1541
# -를 만났을때부터 다음 -까지 최대가 되는 것을 만들면 된다
arr = input().split('-') 
s = 0 
for i in arr[0].split('+'): 
    s += int(i) 
for i in arr[1:]: 
    for j in i.split('+'): 
        s -= int(j) 
print(s)