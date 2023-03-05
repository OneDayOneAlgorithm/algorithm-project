T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    a1,a2,a3 = [[0] * N for _ in range(N)],[[0] * N for _ in range(N)],[[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]        # 이것도 어려움!
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]
    print(f'#{tc}')
    for a,b,c in zip(a1,a2,a3):     # 이거 집 함수가 어려웠음!

        print(f"{''.join(a)} {''.join(b)} {''.join(c)}")
