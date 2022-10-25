# 한줄 수정 문제
def solution(N, votes):
	vote_counter = [0 for i in range(N+1)]
	for i in votes:
		vote_counter[i] += 1

	max_val = max(vote_counter)

	answer = []
	for idx in range(1, N + 1):
		if vote_counter[idx] == max_val:
            #이전
            #answer.append(vote_counter[idx])
            #수정본
			answer.append(idx)
	return answer

N1 = 5
votes1 = [1,5,4,3,2,5,2,5,5,4]
ret1 = solution(N1, votes1)

print("solution 함수의 반환 값은", ret1, "입니다.")

N2 = 4
votes2 = [1, 3, 2, 3, 2]
ret2 = solution(N2, votes2)

print("solution 함수의 반환 값은", ret2, "입니다.")