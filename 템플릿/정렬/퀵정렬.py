# pivot 피벗 = 기준값
# 피벗보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 오도록한다
# 정확히는 피벗 바로 앞, 뒤에 위치
# 마찬가지로 재귀호출로 진행
# 재귀 한번에 무조건 하나의 위치는 정해진다
# 머지 정렬은 쪼개고 합칠 때 정렬을 하지만
# 퀵정렬은 쪼개면서 정렬한다

def swap(ary, i , j):
    ary[i], ary[j] = ary[j], ary[i]

def pivotFirst(ary, left_mark, right_mark):
    pivot_val = ary[left_mark]
    pivot_index = left_mark

    while left_mark <= right_mark:
        while left_mark <= right_mark and ary[left_mark] <= pivot_val:
            left_mark += 1
        while left_mark <= right_mark and ary[right_mark] >= pivot_val:
            right_mark -= 1

        if left_mark <= right_mark:
            swap(ary,left_mark,right_mark)
            left_mark += 1
            right_mark -= 1

    swap(ary,pivot_index,right_mark)    
    return right_mark

def quickSort(ary,pivotMethod=pivotFirst):
    def _qsort(ary,first,last):
        if first < last:
            splitpoint = pivotMethod(ary,first,last)
            _qsort(ary,first,splitpoint-1)
            _qsort(ary,splitpoint+1,last)
    _qsort(ary,0,len(ary)-1)

#테스트
ary = [1,5,2,5,6,77,0,-1,3,4,7,8]

quickSort(ary)

print(ary)
