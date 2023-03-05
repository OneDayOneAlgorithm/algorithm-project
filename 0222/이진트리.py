def func(root,N):
    global cnt
    if root > N:
        return
    func(root*2,N)
    tree[root] = cnt
    cnt += 1
    func(root*2+1,N)


T = int(input())
for tc in range(1,1+T):
    N = int(input())
    tree = [0] * (N + 1)                        # 트리만들기
    cnt = 1
    ans = func(1,N)
    print(f'#{tc} {tree[1]} {tree[N//2]}')