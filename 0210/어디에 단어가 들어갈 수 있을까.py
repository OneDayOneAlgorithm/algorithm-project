import sys
sys.stdin = open('어디에 단어가.txt')
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())        # 가로세로의 길이 // 단어의 길이

    # arr와 arr_t 로 각각 개수를 계산
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    arr_t = list(zip(*arr)) # 대각으로 반전시킴
    total_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):      # 행이 일정할 때 열을 바꿈
            if arr[i][j] == 1:
                cnt += 1
                if cnt == K:
                    total_cnt += 1
                elif cnt > K:
                    total_cnt -= 1
                    cnt = 0
            else:
                cnt = 0
    # print(f'{tc} {total_cnt}')
    for i in range(N):
        cnt = 0
        for j in range(N):  # 행이 일정할 때 열을 바꿈
            if arr_t[i][j] == 1:
                cnt += 1
                if cnt == K:
                    total_cnt += 1
                elif cnt > K:
                    total_cnt -= 1
                    cnt = 0
            else:
                cnt = 0
    print(f'#{tc} {total_cnt}')