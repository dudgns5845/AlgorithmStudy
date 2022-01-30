#문제 https://www.acmicpc.net/problem/2504

#python 리스트에는 단일 변수만 들어가지 않는다
# import sys

# #괄호 입력 받기
# input_list = list(sys.stdin.readline().split())
# temp_stack = []
# result = 0

# #닫힌 괄호가 들어올때 체크를 시작한다
# for c in input_list:
#     if c == ')':
#         #(((()이런 상황이 있을 수 있으므로
#         set_count = 0
#         #(와 [를 저장해놓은 stack을 탐색 시작
#         while len(temp_stack) != 0:
#             #스택 맨위 값 가져오고
#             top = temp_stack.pop()
#             if top == '(':
#                 if set_count == 0:
#                     temp_stack.append(2)
#                 else:
#                     temp_stack.append(2*set_count)
#             elif top == '[':
#                 print(0)
#                 exit(0)
#             else:
#                 set_count = set_count+int(top)
        
#     elif c == ']':
#         #(((()이런 상황이 있을 수 있으므로
#         set_count = 0
#         #(와 [를 저장해놓은 stack을 탐색 시작
#         while len(temp_stack) != 0:
#             #스택 맨위 값 가져오고
#             top = temp_stack.pop()
#             if top == '[':
#                 if set_count == 0:
#                     temp_stack.append(3)
#                 else:
#                     temp_stack.append(3*set_count)
#             elif top == '(':
#                 print(0)
#                 exit(0)
#             else:
#                 set_count = set_count+int(top)


#     # ( [ 일경우
#     else:
#         temp_stack.append(c)

# for i in temp_stack:
#     if i == '(' or i == '[':
#         print(0)
#         exit(0)
#     else:
#         result += i

# print(result)

def solution(s):
    stack = []
    for c in s:
        if c == ')':
            t = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if t == 0 else t*2)
                    break
                elif top == '[':
                    return 0
                else:
                    t += top
        elif c == ']':
            t = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    stack.append(3 if t == 0 else t*3)
                    break
                elif top == '(':
                    return 0
                else:
                    t += top
        else:
            stack.append(c)
        
    return stack

s = input()
stack = solution(s) 
if stack == 0:
    stack = []
print(0 if '(' in stack or '[' in stack else sum(stack))