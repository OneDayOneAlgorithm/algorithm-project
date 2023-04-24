import sys
from collections import deque
import copy
input = sys.stdin.readline

N,M = map(int,input().split())
origin_Map = [list(map(int,input().strip())) for _ in range(N)]
min_v = float('inf')
for i in range(N):
    for j in range(M):
        if origin_Map[i][j] == 1:
            Map = copy.deepcopy(origin_Map)
            Map[i][j] = 0
            q = deque([(0,0)])
            Map[0][0] = 1
            while q:
                cr,cc = q.popleft()  
                if cr == N-1 and cc == M-1:
                    if min_v > Map[N-1][M-1]:
                        min_v = Map[N-1][M-1]  
                    break
                if min_v < Map[cr][cc]:
                    break
                for nr,nc in ((cr+1,cc),(cr-1,cc),(cr,cc+1),(cr,cc-1)):
                    if 0<=nr<N and 0<=nc<M and not Map[nr][nc]:
                        q.append((nr,nc))
                        Map[nr][nc] = Map[cr][cc] + 1      
if min_v == float('inf'):
    print(-1)
else:
    print(min_v)