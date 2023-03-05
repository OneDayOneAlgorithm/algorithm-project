def solve():
    mid = N // 2
    sum_v = 0
    for i in range(N):
        if i <= mid:
            for j in range(mid-i,mid+i+1):
                sum_v += arr[i][j]
        else:
            for j in range(i-mid, N+mid-i):
                sum_v += arr[i][j]
    return sum_v



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    ans = solve()
    print(f'#{tc} {ans}')