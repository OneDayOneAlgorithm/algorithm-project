arr = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9]
]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = 2, 2
for a in range(4):
    print(arr[r + dr[a]][c + dc[a]])
