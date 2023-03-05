import sys
sys.stdin = open('숫자배열회전.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    a1, a2, a3 = [[0] * N for _ in range(N)],[[0] * N for _ in range(N)],[[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a3[i][j] = arr[j][N - 1 - i]
            a2[i][j] = arr[N - 1 - i][N - 1 - j]
            a1[i][j] = arr[N - 1 - j][i]
    result = ''
    print(f'#{tc}')
    for a,b,c in zip(a1,a2,a3):
        print(''.join(a),''.join(b),''.join(c))