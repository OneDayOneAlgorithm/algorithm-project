N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
q = [(0,0)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]
while q:
    cr,cc = q.pop(0)
    for dir in range(4):
        nr = cr + dr[dir]
        nc = cc + dc[dir]
        if 0<=nr<N and 0<=nc<N and board[nr][nc]
        