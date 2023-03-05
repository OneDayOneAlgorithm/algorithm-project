n = int(input())
mountain = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
top = 0
for r in range(n):
    for c in range(n):
        cnt = 0
        for d in range(4):
            nr, nc = r+dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if mountain[r][c] < mountain[nr][nc]:
                    cnt +=1
        if cnt == 0:
            top +=1

print(top)