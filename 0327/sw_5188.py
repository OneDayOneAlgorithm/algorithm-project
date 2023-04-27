def dfs(r,c,sum_v):
    global ans
    if r == N-1 and c== N-1:
        if sum_v < ans:
            ans = sum_v
    if sum_v > ans:
        return
    dr = (1,0)
    dc = (0,1)
    for dir in range(2):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr > N-1 or nc > N-1:
            continue
        if not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr,nc,sum_v+arr[nr][nc])
            visited[nr][nc] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 12*12*10
    visited = [[0]*N for _ in range(N)]
    dfs(0,0,arr[0][0])
    print(f'#{tc} {ans}')
