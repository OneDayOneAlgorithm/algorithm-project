def inorder(i, arr):
    N = len(arr)
    if not N:
        return
    if N == 1:
        tree[i] = arr[0]
    else:
        tree[i] = arr[N//2]
        inorder(i*2, arr[:N//2])
        inorder((i*2)+1, arr[(N//2)+1:])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    arr = [i for i in range(1, N+1)]
    inorder(1, arr)
    print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')



















