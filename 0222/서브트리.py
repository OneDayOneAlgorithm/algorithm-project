
def func(N):
    global cnt
    if N == 0:
        return
    cnt += 1
    func(tree[0][N])
    func(tree[1][N])

T = int(input())
for tc in range(1,T+1):
    cnt = 0
    E,N = map(int,input().split())
    tree = [[0]*(E+2) for _ in range(2)]
    arr = list(map(int,input().split()))
    for i in range(0,E*2,2):
        if tree[0][arr[i]] != 0:
            tree[1][arr[i]] = arr[i+1]
        else:
            tree[0][arr[i]] = arr[i+1]
    func(N)
    print(f'#{tc} {cnt}')























