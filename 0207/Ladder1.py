for _ in range(10):
    T = int(input())
    for _ in range(100):
        arr = list(map(int,input().split()))
    dr = [0, 0, -1]  # 우 좌 상
    dc = [1, -1, 0]
    for j in range(100):
        if arr[99][j] == 2:
            tmp = j
    #도착지점 좌표 정해주기
    r,c = 99,j  
    dir = 0
    while r > 0:
        r2 = r + dr[dir]
        c2 = r + dr[dir]
        if 0 <=r2 < 100 and 0<= c2 <100 and arr[r][c]:
            r = r2
            c = c2
            dir = 0
        else:
            dir = (dir+1) % 3
    print(f'#{T} {c}')