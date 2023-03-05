'''
모든 시작점, K를 넓혀가면서...
for i (si-K+1, si+K)
for j (sj-K+1+, sj+K-)

'''


def solve_loop():
    mx = 0
    for si in range(N):
        for sj in range(N):  # 가능한 모든 시작위치
            for k in range(1, 2 * N):
                cnt = 0
                for i in range(si - k + 1, si + k):
                    t = abs(si - i)
                    for j in range(sj - k + 1 + t, sj + k - t):
                        if 0 <= i < N and 0 <= j < N:
                            cnt += arr[i][j]  # 집위치를 더하기(집이 1이니 집 개수 추가)
                # 운영비용 보다 수익이 같거나 큰 경우 정답갱신
                if ((k * k) + (k - 1) * (k - 1)) <= cnt * M:
                    mx = max(mx, cnt)
    return mx


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # M: 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve_loop()
    print(f'#{test_case} {ans}')