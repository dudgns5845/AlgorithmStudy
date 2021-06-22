#처음부터 끝까지 정렬이 아니라
#인덱스를 하나씩 늘려가면서 그 안에서 정렬을 진행하는 것이다.
#데이터가 이미 정렬 되어있다면 세로운 데이터 삽입시 정렬이 O(n)으로 빠르다
#그러나 역순으로 정렬되었다면 O(n*n)이다

def insertionSort(ary):
    for size in range(1,len(ary)):
        val = ary[size]
        i = size
        while i > 0 and ary[i-1] > val:
            ary[i] = ary[i-1]
            i -= 1
            ary[i] = val

#테스트
ary = [1,5,2,5,6,77,0,-1,3,4,7,8]

insertionSort(ary)

print(ary)
    