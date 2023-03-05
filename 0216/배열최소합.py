T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # idx 행의 몇 번째 열을 선택할건지 결정
    # selected = [-1] * N    [0,-1,-1,-1,-1]
    used = [0] * N
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_sum = 1000
    def solve(idx,sum_v):
        global min_sum
        # 가능성이 없는 경우의 수는 수행하지 않음 : 가지치기
        # 이미 구한 최소값보다 중간 합이 더 크거나 같음
        if sum_v >= min_sum:
            return

        if idx == N:
            #모든 행을 다 결정한거니까...
            # sum_v = 0
            # for i in range(N):
            #     # selected[i] # i 행에서 선택한 열
            #     sum_v += arr[i][selected[i]]
            # print(selected, sum_v)
            if min_sum > sum_v:
                min_sum = sum_v
            return
        # 내가 할 수 있는 모든 경우의 수 수행해보기
        for i in range(N):  #i 열의 번호, 모든 열 선택
            if not used[i]:
                # selected[idx] = i
                used[i] = 1
                solve(idx+1, sum_v + arr[idx][i])
                used[i] = 0

    # 더한게 없으니 중간합은 0
    solve(0,0)
    print(f'#{tc} {min_sum}')



























