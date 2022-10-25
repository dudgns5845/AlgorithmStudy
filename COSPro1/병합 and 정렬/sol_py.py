def solution(arrA, arrB):
	arrA_idx = 0
	arrB_idx = 0
	arrA_len = len(arrA)
	arrB_len = len(arrB)
	answer = []
	while arrA_idx < arrA_len and arrB_idx < arrB_len :
		if arrA[arrA_idx] < arrB[arrB_idx]:
			answer.append(arrA[arrA_idx])
			arrA_idx += 1
		else:
			answer.append(arrB[arrB_idx])
			arrB_idx += 1
	while arrA_len > arrA_idx:
		answer.append(arrA[arrA_idx])
		arrA_idx += 1
	while arrB_len > arrB_idx:
		answer.append(arrB[arrB_idx])
		arrB_idx += 1
	return answer

arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution(arrA, arrB);

print("solution 함수의 반환 값은", ret, "입니다.")