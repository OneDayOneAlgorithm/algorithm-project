def dfs(n, sm):
    global ans
    if n == N:
        if sm >= B:
            if sm-B < ans:
                ans = sm-B
        return
    if sm-B > ans:
        return
    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 999999999999
    dfs(0, 0)
    print(f'#{tc} {ans}')
