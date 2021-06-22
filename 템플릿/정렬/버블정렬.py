# 맨 처음 앞부터 시작해 끝까지 진행을 하면서 이웃한 두개를 비교하면서 정렬을 진행을 한다
# 복잡도 O(n*n)
#swap 메소드
#ary는 리스트, i,j는 인덱스
def swap(ary,i,j):
    ary[i], ary[j] = ary[j], ary[i]

def bubbleSort(ary):
    for size in reversed(range(len(ary))):
        for i in range(size):
            if ary[i] > ary[i+1]:
                swap(ary, i,i+1)

#테스트
ary = [1,5,2,5,6,77,0,-1,3,4,7,8]

bubbleSort(ary)

print(ary)
