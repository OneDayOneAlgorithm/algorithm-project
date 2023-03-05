T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    for i in range(1,N):
        for j in range(N):
            if j == 0:
                arr[i][j] = 1
            else:   # 윗 행의 바로 윗열과 왼쪽열을 더한다
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()

