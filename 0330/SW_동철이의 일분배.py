def solve(n, sum_v):
    global max_v
    if n == N:
        if max_v < sum_v:
            max_v = sum_v
        return
    if sum_v <= max_v:
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            solve(n+1, sum_v*arr[n][i]*0.01)
            used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    used = [0] * N
    solve(0, 1)
    print(f'#{tc} {max_v*100:.6f}')
