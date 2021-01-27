arr=[]
 
a=input()
b=input().split()
 
n=int(a)
for i in range(n) :
    arr.append(int(b[i]))
 
i=n-1
while i>=0 :
    print(arr[i], end=' ')
    i-=1
     
