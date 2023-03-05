import sys
sys.stdin = open('어디에 단어가.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) + [0] for _ in range(N)] + [[0] * N]
    arr_t = list(map(list,zip(*arr)))
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(N+1):
            if arr_t[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
    print(f'#{tc} {result}')
