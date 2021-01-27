input = int(input())
sum =0
for i in range(1,input+1):
    sum += i
    if(sum >= input):
        print(sum)
        break
