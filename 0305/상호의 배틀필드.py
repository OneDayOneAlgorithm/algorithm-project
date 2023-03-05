T = int(input())
for tc in range(1,T+1):
    H,W = map(int,input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    commend = input()
    for r in range(H):
        for c in range(W):
            if arr[r][c] in ('>', '<', '^', 'v'):
                cr, cc = r, c
                break
    for key in commend:
        dr,dc = [-1,1,0,0],[0,0,-1,1]
        if key == 'U':
            nr,nc = cr+dr[0],cc+dc[0]
            if 0<=nr<H and 0<=nc<W and arr[nr][nc] and arr[nr][nc] == '.':
                arr[cr][cc] = '.'
                arr[nr][nc] = '^'
                cr,cc = nr,nc
            else:
                arr[cr][cc] = '^'
        if key == 'D':
            nr,nc = cr+dr[1],cc+dc[1]
            if 0<=nr<H and 0<=nc<W and arr[nr][nc] and arr[nr][nc] == '.':
                arr[cr][cc] = '.'
                arr[nr][nc] = 'v'
                cr, cc = nr, nc
            else:
                arr[cr][cc] = 'v'
        if key == 'L':
            nr,nc = cr+dr[2],cc+dc[2]
            if 0<=nr<H and 0<=nc<W and arr[nr][nc] and arr[nr][nc] == '.':
                arr[cr][cc] = '.'
                arr[nr][nc] = '<'
                cr, cc = nr, nc
            else:
                arr[cr][cc] = '<'
        if key == 'R':
            nr,nc = cr+dr[3],cc+dc[3]
            if 0<=nr<H and 0<=nc<W and arr[nr][nc] and arr[nr][nc] == '.':
                arr[cr][cc] = '.'
                arr[nr][nc] = '>'
                cr, cc = nr, nc
            else:
                arr[cr][cc] = '>'
        if key == 'S':
            if arr[cr][cc] == '<':
                nr,nc = cr,cc-1
                while 0<=nr<H and 0<=nc<W:
                    if arr[nr][nc] == '#':
                        break
                    if arr[nr][nc] == '*':
                        arr[nr][nc] = '.'
                        break
                    nc -= 1
        if key == 'S':
            if arr[cr][cc] == '>':
                nr,nc = cr,cc+1
                while 0<=nr<H and 0<=nc<W:
                    if arr[nr][nc] == '#':
                        break
                    if arr[nr][nc] == '*':
                        arr[nr][nc] = '.'
                        break
                    nc += 1
        if key == 'S':
            if arr[cr][cc] == '^':
                nr,nc = cr-1,cc
                while 0<=nr<H and 0<=nc<W:
                    if arr[nr][nc] == '#':
                        break
                    if arr[nr][nc] == '*':
                        arr[nr][nc] = '.'
                        break
                    nr -= 1
        if key == 'S':
            if arr[cr][cc] == 'v':
                nr,nc = cr+1,cc
                while 0<=nr<H and 0<=nc<W:
                    if arr[nr][nc] == '#':
                        break
                    if arr[nr][nc] == '*':
                        arr[nr][nc] = '.'
                        break
                    nr +=1
    print(f'#{tc} ',end='')
    for i in range(H):
        print(''.join(arr[i]))




