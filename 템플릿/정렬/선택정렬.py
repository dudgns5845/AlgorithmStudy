# 배열에서 최댓값을 먼저 찾아 맨 오른쪽과 교체한다
# 최소값일 경우는 왼쪽과 교체
# 대체로 버블 정렬보다는 빠르지만 
# 복잡도는 마찬가지 O(n*n)

def swap(ary,i,j):
    ary[i] ,ary[j] = ary[j], ary[i]

def selectionSort(ary):
    for size in reversed(range(len(ary))):
        #최대값의 인덱스
        max_i = 0
        for i in range(1,1+size):
            if ary[i] > ary[max_i]:
                max_i = i
                
            swap(ary,max_i,size)

#테스트
ary = [1,5,2,5,6,77,0,-1,3,4,7,8]

selectionSort(ary)

print(ary)
