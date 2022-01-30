#문제 url - https://www.acmicpc.net/problem/14888

#n = int(input())


#유클리드 호제법 코드로 구현해보기

a,b = map(int,input().split())

#최소공배수 구하기
def gcd(a,b):
    # if(a<b):
    #     a , b = b , a
    if a % b == 0:
        return b
    else:
        print(a,b)
        gcd(b,a%b)

print(gcd(a,b))    

