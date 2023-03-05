T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    first_value = 0
    for i in range(M):
        first_value += arr[i]

    max_v = first_value
    min_v = first_value
    print(max_v,min_v)

    for i in range(1, N - M + 1):
        sum = 0
        for j in range(i, i + M):
            sum += arr[j]

        if max_v < sum:
            min_v = sum
        if min_v > sum:
            min_v = sum

    ans = max_v - min_v
    print(f'#{tc} {ans}')