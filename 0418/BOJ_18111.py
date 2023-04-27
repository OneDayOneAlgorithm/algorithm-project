import sys
input = sys.stdin.readline

def solve(s,e,B):
    c = s
    min_vv = 99999
    result = []
    for c in range(s,e+1):
        block = B
        cnt = 0
        for i in range(N):
            for j in range(M):
                if c > ground[i][j]:
                    cnt += (c - ground[i][j])
                    block -= (c - ground[i][j])
                else:
                    cnt += (ground[i][j] - c)*2
                    block += (ground[i][j] - c)
        if block >= 0:
            min_vv = cnt
            lst.append((cnt,c))
        c += 1

N,M,B = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
lst = []
solve(B)


N,M,B = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
e = 0
s = 99999
for i in range(N):
    for j in range(M):
        if e < ground[i][j]:
            e = ground[i][j]
        if s > ground[i][j]:
            s = ground[i][j]
lst = solve(s,e,B)



