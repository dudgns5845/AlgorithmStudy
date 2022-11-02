def solution(babbling):
    answer = 0
    word_list = ["aya", "ye", "woo", "ma"]
    
    for babble in babbling:
        for word in word_list:
            if word*2 not in babble:
                babble = babble.replace(word," ")
        if len(babble.strip()) == 0:
            answer+=1
    return answer

# 좌우 문자열 싹다 제거 
# strip() -> replace(word, " ") -> 공백을 줄것

# from itertools import permutations

# def solution(babbling):
#     answer = 0
#     word_list = ["aya", "ye", "woo", "ma","","","",""]
    
#     words = list(permutations(word_list,4))
    
#     real_word = set()
#     for word in words:
#         temp = ""
#         for w in word:
#             temp += w
#         if temp != "":
#             real_word.add(temp)
#     real_word = sorted(list(real_word))
    
#     for babble in babbling:
#         if babble in real_word:
#             answer += 1
#     return answer