#bottomup  방식
input = int(input())

food = list(map(int,input().split())

mem = [0] * 1000

mem[0] = food[0]
mem[1] = max(food[0],food[1])

for i in range (2,n):
    mem[i] = max(mem[i-2],mem[i-1] + food[i] ) 

print(mem[input-1])

