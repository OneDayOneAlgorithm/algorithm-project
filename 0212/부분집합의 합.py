T = int(input())
for tc in range(1, T + 1):
    N, K = map(int,input().split())
    result = 0
    for i in range(1<<12):  # 총 범위
        sum = 0
        cnt = 0
        for j in range(12):  # 원소의 갯수
            if i & 1<<j:
                sum += j+1
                cnt += 1
        if sum == K and cnt == N:
            result += 1
    print(f'#{tc} {result}')