import sys
input = sys.stdin.readline
def solve(s,e,B):
    c = s
    while c<=e:
        block = 0
        block += B
        cnt = 0
        mid = c
        for i in range(N):
            for j in range(M):
                if mid > ground[i][j]:
                    cnt += (mid - ground[i][j])
                    block -= (mid - ground[i][j])
                elif mid < ground[i][j]:
                    cnt += (ground[i][j] - mid)*2
                    block += (ground[i][j] - mid)
        if block >= 0:
            lst.append((cnt,mid))
        c += 1

N,M,B = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
e = 0
s = 999999
for i in range(N):
    for j in range(M):
        if e < ground[i][j]:
            e = ground[i][j]
        if s > ground[i][j]:
            s = ground[i][j]
lst = []
solve(s,e,B)
lst.sort(key=lambda x:x[1])
lst.sort(key=lambda x:x[0])
print(*lst[0])



