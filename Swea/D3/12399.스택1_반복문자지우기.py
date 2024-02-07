# for tc in range(1, int(input())+1):
#     def push(item):
#         global top
#         top += 1
#         stack[top] = item
#
#     def pop():
#         global top
#         stack[top] = 0
#         top -= 1
#
#     top = -1 # push가 실행되면 stack[0]을 확인
#     strLst = list(input()) # 문자받기
#     N = len(strLst) # 문자길이, 사이즈
#     stack = [0] * N # 스택
#
#     cnt = 0
#     for i in strLst: # 넣을 문자열을 돈다
#         push(i) # stack의 0번째에 i를 넣음, top = 0부터
#         prev = top - 1 # 스택의 top과 그 이전을 비교
#         if 0 <= prev:
#             if stack[prev] == stack[top]:
#                 pop()
#                 top -= 1
#                 cnt += 1
#         print(stack, top)

# state 2
T = int(input())
for tc in range(1, T+1):
    str_lst = input()
    stack = [0] * len(str_lst)
    top = -1

    def push(item):
        global top
        top += 1
        stack[top] = item
    def pop():
        global top
        stack[top] = 0
        top -= 1

    for i in str_lst:
        if stack[top] != i:
            push(i)
        elif i == stack[top]:
            pop()
    
    cnt = 0
    for j in stack:
        if j != 0:
            cnt += 1

    print(f'#{tc} {cnt}')