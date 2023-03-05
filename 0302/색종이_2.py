N = int(input())
board = [[0]*102 for _ in range(102)]
for _ in range(N):
    a,b = map(int,input().split())
    for i in range(b+1,b+11):
        for j in range(a+1,a+11):
            board[i][j] = 1
cnt = 0
for i in range(102):
    c= 0
    for j in range(102):
        if board[i][j] != c:
            c = not c
            cnt += 1

for j in range(102):
    c=0
    for i in range(102):
        if board[i][j] != c:
            c = not c
            cnt += 1
print(cnt)