import sys
sys.stdin = open('input (1).txt')
T = 10
for tc in range(1, 1 + T):
    N = int(input())
    arr = [input() for i in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(9-N):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                cnt += 1
    for j in range(8):
        for i in range(9-N):
            lst = []
            for k in range(N):
                lst.append(arr[i + k][j])
            if lst == lst[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')
