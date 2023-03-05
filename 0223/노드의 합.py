# def func(N):
#     if N > n:
#         return 0
#     tree[N] += func(N*2) + func(N*2+1)
#     return tree[N]
# T = int(input())
# for tc in range(1,T+1):
#     n,M,L = map(int,input().split())    # 노드의 개수, 리프노드의 개수, 출력할 노드번호
#     tree = [0] * (n + 1)
#     for i in range(M):
#         a, b = map(int,input().split())     # 리프 노드 번호
#         tree[a] = b
#
#     func(1)
#
#     print(f'#{tc} {tree[L]}')




def solve(n):
    if n>N or tree[n] != 0:
        return
    solve(n*2)
    solve(n*2+1)
    tree[n] = tree[n*2] + tree[n*2+1]


T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    tree = [0] * (N+2)
    for i in range(M):
        a,b = map(int,input().split())
        tree[a] = b
    solve(1)
    print(f'#{tc} {tree[L]}')



























