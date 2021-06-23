from collections import deque

temp = [1,2,3,4,5,6,7,8,9]
temp_1 = []
for i , v in enumerate(temp):
    temp_1.append([v,i])

#temp_1.sort(reverse=True)
#두번째 인자로 정렬하기, 역순으로 정렬하기
temp_1.sort(key= lambda element: element[1], reverse= True)
print(temp_1)


#정렬 관련 참고 
#https://twpower.github.io/118-sort-list-elements-by-using-key