T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    lst = []
    for _ in range(N):
        lst.append(input())
    for i in range(N):
        for j in range(N - M + 1):
            if lst[i][j : j + M] == lst[i][j : j + M][::-1]:
                word = lst[i][j : j + M]
    for j in range(N):
        for i in range(N - M + 1):
            lst1 = []
            for k in range(M):
                lst1.append(lst[i+k][j])
            if lst1 == lst1[::-1]:
                # word = l
                # word = ''.join(lst1)
                print(f'#{tc} {word}')
