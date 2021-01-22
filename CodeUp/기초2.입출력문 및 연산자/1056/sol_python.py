a,b=input().split()

x=int(a)
y=int(b)
b1=bool(x)
b2=bool(y)

z=int((b1==True and b2==False) or (b1==False and b2==True))

print(z)
