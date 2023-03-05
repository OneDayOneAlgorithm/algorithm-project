import sys
sys.stdin = open('노드의 거리.txt')
# def func(arr,S,V,Ed):
#     p = [S]
#     visited = [0] * (V+1)
#     visited[S] = 1
#     while p:
#         a = p.pop(0)
#         for i in range(V+1):
#             if not visited[i] and arr[a][i]:
#                 p.append(i)
#                 visited[i] = 1 + visited[a]
#                 if i == Ed:
#                     return visited[i]-1
#     return 0
#
#
# T = int(input())
# for tc in range(1,1+T):
#     V,E = map(int,input().split())
#     arr = [[0] * (V+1) for _ in range(V+1)]
#     for i in range(E):
#         a,b = map(int,input().split())
#         arr[a][b] = 1
#         arr[b][a] = 1
#     S,Ed = map(int,input().split())
#     ans = func(arr,S,V,Ed)
#     print(f'#{tc} {ans}')


def solve(S,G):
    q = [S]
    visited[S] = 1
    while q:
        c = q.pop(0)
        for i in arr[c]:
            if i == G:
                return visited[c]
            elif visited[i] == 0:
                q.append(i)
                visited[i] = visited[c] + 1
    return 0
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr = [[] for _ in range(V+1)]
    for i in range(E):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    S,G = map(int,input().split())
    visited = [0] * (V+1)
    print(f'#{tc} {solve(S,G)}')



























