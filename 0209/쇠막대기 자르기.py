T = int(input())
for tc in range(1, T + 1):
    arr = input()
    N = len(arr)
    cnt = 0
    parts = 0
    for i in range(N):
        if arr[i] == '(':
            cnt += 1    # 기본적으로 cnt + 1
            if i > 0 and arr[i-1] == '(':  # ((일 때 parts += 1
                parts += 1
        elif arr[i] == ')':
            if arr[i-1] == '(':  # ()일 때 part += cnt - 1
                parts += cnt-1
            cnt -= 1    # 기본적으로 cnt -1
    print(f'#{tc} {parts}')
