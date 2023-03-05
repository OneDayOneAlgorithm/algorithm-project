T = int(input())
for tc in range(T):
    N = int(input())
    a = list(map(int, input()))
    cnt = [0]*10
    for i in a:
        cnt[i] += 1  # cnt[9] = 2

    max = cnt[0]
    for i in cnt:
        if max < i:
            max = i  # max = 2

    for i in range(len(cnt)):
        if cnt[i] == max:
            max_1 = i
    print(f'#{tc+1} {max_1} {max}')
