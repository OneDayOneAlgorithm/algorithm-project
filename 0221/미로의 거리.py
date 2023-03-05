import sys
sys.stdin = open('미로의 거리.txt')
# def func(arr,N):
#     for r in range(N):
#         for c in range(N):
#             if arr[r][c] == 2:
#                 sr,sc = r,c
#             if arr[r][c] == 3:
#                 er,ec = r,c
#     visited = [[0] * N for _ in range(N)]
#     q = [(sr,sc)]
#     dr = [1,-1,0,0]
#     dc = [0,0,1,-1]
#     visited[sr][sc] = 1
#     while q:
#         cr,cc = q.pop(0)
#         if arr[cr][cc] == 3:
#             return visited[cr][cc] - 2
#         for dir in range(4):
#             nr,nc = cr + dr[dir], cc + dc[dir]
#             if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and arr[nr][nc] != 1:
#                 visited[nr][nc] = 1 + visited[cr][cc]
#                 q.append((nr,nc))
#     return 0
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int,input())) for _ in range(N)]
#     ans = func(arr,N)
#     print(f'#{tc} {ans}')

def func(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                q = [(i,j)]
                visited[i][j] = 1
    dr,dc = [0,0,1,-1],[1,-1,0,0]
    while q:
        cr,cc = q.pop(0)
        for dir in range(4):
            nr,nc = cr + dr[dir], cc+dc[dir]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] != '1' and not visited[nr][nc]:
                if arr[nr][nc] == '3':
                    return visited[cr][cc] -1
                else:
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr,nc))
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visited = [[0]*(N+1) for _ in range(N+1)]
    arr = [input() for _ in range(N)]
    ans = func(arr)
    print(f'#{tc} {ans}')




















