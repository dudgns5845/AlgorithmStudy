a,b,c = map(int,input().split(" "))
i = 1
while True:
    if(i%a == 0 and i%b == 0 and i%c ==0):
        print(i)
        break
    i+=1