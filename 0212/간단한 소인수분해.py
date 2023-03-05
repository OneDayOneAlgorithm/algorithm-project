T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = []
    cnt = [0] * 12
    break_cnt = 0
    while break_cnt<5:
        break_cnt = 0
        for i in (2,3,5,7,11):
            if N % i == 0:
                cnt[i] += 1
                N = N // i
            else:
                break_cnt += 1
    for i in (2,3,5,7,11):
        result.append(cnt[i])
    print(f'#{tc}', *result)