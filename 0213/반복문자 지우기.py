T = int(input())
for tc in range(1, T + 1):
    arr = input()
    stack = []
    for i in arr:
        if stack:                   # 빈 스택이 아닐 때
            if stack[-1] == i:      # 현재 문자와 top이 일치한다면
                stack.pop()         # 팝
            else:
                stack.append(i)     # 다르면 어팬드
        else:
            stack.append(i)         # 빈 리스트면 어팬드
    print(f'#{tc} {len(stack)}')






