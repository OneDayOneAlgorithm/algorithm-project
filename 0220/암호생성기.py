for tc in range(1,11):
    T = int(input())
    arr = list(map(int,input().split()))
    i = 1
    while arr[-1] != 0:
        if arr[0] >= i:
            arr[0] = arr[0]-i
        else:
            arr[0] = 0
        arr.append(arr.pop(0))
        i = (i + 1) % 6
        if i % 6 == 0:
            i += 1
    print(f'#{tc}',*arr)
