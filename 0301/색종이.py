N = int(input())
board = [[0] * 100 for _ in range(100)]
for i in range(N):
    a,b = map(int,input().split())
    for i in range(89-b,99-b):
        for j in range(a-1,a+9):
            board[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            cnt += 1
print(cnt)