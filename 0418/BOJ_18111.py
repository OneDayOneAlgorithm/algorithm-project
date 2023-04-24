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
                elif c < ground[i][j]:
                    cnt += (ground[i][j] - c)*2
                    block += (ground[i][j] - c)
        if block < 0 :
            continue
        if cnt < min_vv:
            min_vv = cnt
            result.append((min_vv, c))
    return result

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
lst.sort(key=lambda x:x[1], reverse=True)
lst.sort(key=lambda x:x[0])
print(*lst[0])



