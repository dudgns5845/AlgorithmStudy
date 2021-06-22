# 두 부분으로 재귀적을 쪼개고, 반대로 두개씩 비교를 진행하면서 정렬하고 병합해나가는 분할정복 알고리즘
# 복잡도 O(n/logn)
# 메모리가 많이 필요하다는게 단점

def mergeSort(ary):

    if len(ary) > 1:
        #중간 찾고
        mid = len(ary)//2
        # 중간 기준으로 좌우 쪼개기
        left_ary , right_ary = ary[:mid] , ary[mid:]
        
        #배열의 인자가 1개일때까지 재귀 반복
        mergeSort(left_ary) #왼쪽부터 재귀
        mergeSort(right_ary) # 오른쪽 재귀

        #병합 진행
        left_index , right_index , index = 0, 0, 0

        while left_index < len(left_ary) and right_index < len(right_ary):
            if left_ary[left_index] < right_ary[right_index]:
                ary[index] = left_ary[left_index]
                left_index += 1

            else:
                ary[index] = right_ary[right_index]
                right_index += 1
            index += 1
        ary[index:] = left_ary[left_index:] if left_index != len(left_ary) else right_ary[right_index:]

#테스트
ary = [1,5,2,5,6,77,0,-1,3,4,7,8]

mergeSort(ary)

print(ary)
