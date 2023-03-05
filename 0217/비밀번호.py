for tc in range(1,11):
    N,arr = map(int,input().split())
    stack = []
    for i in str(arr):
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    result = ''.join(stack)
    print(f'#{tc} {int(result)}')

