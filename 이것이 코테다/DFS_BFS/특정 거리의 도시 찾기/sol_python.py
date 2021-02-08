# N:도시의 개수 M: 도로의 개수 K: 거리 정보 X: 출발 도시의 번
N, M, K, X = map(int, input().split(" "))

street = []

#지도 생성
for i in range(N+1):
    street.append([])
    for _ in range(N+1):
        street[i].append(0)

for i in range(1,N+1):
    for j in range(1,N+1):
        print(street[i][j] )
    print()


