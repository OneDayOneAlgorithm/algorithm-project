import sys

sys.stdin = open('미로1.txt')

<<<<<<< HEAD
# def func(arr):
#     for r in range(16):
#         for c in range(16):
#             if arr[r][c] == 2:
#                 cr,cc = r,c
#     visited = [[0] * 16 for _ in range(16)]
#     dr = [1,-1,0,0]
#     dc = [0,0,1,-1]
#     q = [(cr,cc)]
#     visited[cr][cc] = 1
#     while q:
#         cr,cc = q.pop(0)
#         if arr[cr][cc] == 3:
#             return 1
#         for dir in range(4):
#             nr,nc = cr+dr[dir], cc+dc[dir]
#             if 0<=nr<16 and 0<=nc<16 and not visited[nr][nc] and arr[nr][nc] != 1:
#                 q.append((nr,nc))
#                 visited[nr][nc] = 1
#     return 0
#
# for tc in range(1,11):
#     T = int(input())
#     arr = [list(map(int,input())) for _ in range(16)]
#     result = func(arr)
#     print(f'#{tc} {result}')





def func(arr):
    cr,cc = 1,1
    p = [(cr,cc)]
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    visited = [[0] * 16 for _ in range(16)]
    while p:
        cr,cc = p.pop(0)
        if arr[cr][cc] == 3:
            return 1
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if 0<=nr<16 and 0<=nc<16 and not visited[nr][nc] and arr[nr][nc] != 1:
                p.append((nr,nc))
                visited[nr][nc] = 1 + visited[cr][cc]
    return 0
for tc in range(1,11):
    T = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    ans = func(arr)
    print(f'{tc} {ans}')


































=======
def func(arr):
    for r in range(16):
        for c in range(16):
            if arr[r][c] == 2:
                cr,cc = r,c
    visited = [[0] * 16 for _ in range(16)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    q = [(cr,cc)]
    visited[cr][cc] = 1
    while q:
        cr,cc = q.pop(0)
        if arr[cr][cc] == 3:
            return 1
        for dir in range(4):
            nr,nc = cr+dr[dir], cc+dc[dir]
            if 0<=nr<16 and 0<=nc<16 and not visited[nr][nc] and arr[nr][nc] != 1:
                q.append((nr,nc))
                visited[nr][nc] = 1
    return 0

for tc in range(1,11):
    T = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    result = func(arr)
    print(f'#{tc} {result}')
>>>>>>> e7acc587f08a3fe10286ca9fe261209ccd590371

