T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = b = c = d = e = 0
    while True:
        stop = 0
        # 5가 되면 종료
        if N % 2 == 0:
            N = N // 2
            a += 1
        else:
            stop += 1
        if N % 3 == 0:
            N = N // 3  
            b += 1
        else:
            stop += 1
        if N % 5 == 0:
            N = N // 5
            c += 1
        else:
            stop += 1
        if N % 7 == 0:
            N = N // 7
            d += 1
        else:
            stop += 1
        if N % 11 == 0:
            N = N // 11
            e += 1
        else:
            stop += 1
        if stop == 5:
            break
    print(f'#{tc} {a} {b} {c} {d} {e}')