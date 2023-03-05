T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = input()
    cnt = 0
    max = 0
    for i in range(N):
        if arr[i] == '1':
            cnt += 1
            if max < cnt:
                max = cnt
        else:
            cnt = 0
    print(f'#{tc} {max}')