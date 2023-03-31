def dfs(n, sm):
    global ans
    if n >= 12:
        if sm < ans:
            ans = sm
        return
    if sm > ans:
        return

    dfs(n+1, sm+day*lst[n-1])
    dfs(n+1, sm+month)
    dfs(n+3, sm+month_3)
    dfs(n+12, sm+year)


T = int(input())
for tc in range(1, T+1):
    day, month, month_3, year = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 365*3000
    dfs(0, 0)
    print(f'#{tc} {ans}')
