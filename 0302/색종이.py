import sys
N = int(sys.stdin.readline())
board = [[-1] * 1001 for _ in range(1001)]
for k in range(N):
    a,b,c,d = map(int,sys.stdin.readline().split())
    for i in range(a,a+c):
        for j in range(b,b+d):
            board[i][j] = k
for k in range(N):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == k:
                cnt += 1
    print(cnt)