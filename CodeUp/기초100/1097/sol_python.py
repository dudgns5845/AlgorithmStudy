m=[]
for i in range(20) :
    m.append([])
    for j in range(20) :
        m[i].append(0)

for i in range(19) :
    a=input().split()
    for j in range(19) :
        m[i+1][j+1]=int(a[j])
    
n=int(input())

for i in range(n) :
    x,y=input().split()
    for j in range(1, 20) :
        
        if m[j][int(y)]==0 :
            m[j][int(y)]=1
        else :
            m[j][int(y)]=0

        if m[int(x)][j]==0 :
            m[int(x)][j]=1
        else :
            m[int(x)][j]=0

for i in range(1, 20) :
    for j in range(1, 20) :
        print(m[i][j], end=' ')
    print()
            

