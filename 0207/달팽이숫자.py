N = int(input())
arr = [[0 for i in range(N)]for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c = 0, 0
dir = 0
for i in range(1, N*N+1):
    arr[r][c] = i
    next_r = r + dr[dir]
    next_c = c + dc[dir]
    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N or arr[next_r][next_c] != 0:
        dir = (dir+1) % 4
    r, c = r + dr[dir], c + dc[dir]
print(arr)

