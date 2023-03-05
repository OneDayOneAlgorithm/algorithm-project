import sys
sys.stdin = open('스도쿠검증.txt')
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    arr_t = list(zip(*arr))     # zip하면 리스트를 풀어서 순서없는 여러 튜플형태로 묶는다
    cnt = 0
    for i in range(9):
        if len(set(arr[i])) != 9:
            cnt += 1
            break
    for i in range(9):
        if len(set(arr_t[i])) != 9:
            cnt += 1
            break        

    for i in (0,3,6):
        for j in range(0,3,6):
            if len(set(arr[i][j:j+3]+arr[i+1][j:j+3]+arr[i+2][j:j+3])) != 9:
                cnt += 1
                break
    if cnt == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

