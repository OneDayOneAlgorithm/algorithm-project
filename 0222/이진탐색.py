# def func(p):
#     global cnt
#     if p > N:
#         return
#     func(p * 2)
#     tree[p] = cnt
#     cnt += 1
#     func(p*2 +1)
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     tree = [0] * (N + 1)
#     cnt = 1
#     func(1)
#     print(f'#{tc} {tree[1]} {tree[N//2]}')

def solve(S):
    global cnt
    if S > N:
        return
    solve(S*2)
    cnt += 1
    tree[S] = cnt
    solve(S * 2+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 0
    solve(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')





















