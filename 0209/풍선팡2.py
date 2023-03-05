T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    di = [0,1,0,-1] # 우하좌상
    dj = [1,0,-1,0]
    i,j = 0,0
    dir = 0
    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            for _ in range(4):         #한 지점에서 우하좌상 값의 합
                next_i = i + di[dir]
                next_j = j + dj[dir]
                if next_i < 0 or next_i >=N or next_j < 0 or next_j >= M:   # 범위 밖으로 나갈 시 패쓰
                    dir = (dir + 1) % 4
                else:
                    i = next_i
                    j = next_j
                    sum += arr[i][j]
                    i = i - di[dir]
                    j = j - dj[dir]
                    dir = (dir + 1) % 4 # 우하좌상 방향전환
            lst.append(sum)
    print(f'#{tc} {max(lst)}') # max 써서 죄송해요 자고 일어나서 고칠게요!