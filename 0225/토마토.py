from collections import deque
def solve(arr):
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))
                visited[i][j] = 1
            elif arr[i][j] == -1:
                visited[i][j] = -1

    dr,dc = [0,0,-1,1],[-1,1,0,0]
    while q:
        cr,cc = q.popleft()
        for dir in range(4):
            nr,nc = cr + dr[dir],cc+dc[dir]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0:
                arr[nr][nc] = 1
                visited[nr][nc] = visited[cr][cc] + 1
                q.append((nr,nc))
    for k in visited:
        if 0 in k:
            return -1
    return visited[cr][cc] - 1




M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)]
print(solve(arr))