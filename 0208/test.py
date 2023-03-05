import sys
sys.stdin = open('input_ladder.txt')
T = 10
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    # 시작 점 찾기 : 0번행에서 1인 인덱스 찾기
    # 0번 : 하, 1번: 좌, 2번: 우
    dr = [1,0,0]
    dc = [0,-1,1]
    result = -1
    for i in range(100):
        if ladder[0][i] == 1:
        # 시작점 마다 사다리 타기 시작
            dir = 0 #아래 방향 시작
            r,c = 0,i   #시작점 지정
            #한 칸 씩 이동하기 를 반복 >>> 목적지 도착하기 전까지
            # r이 99행이 될 때 까지 반복
            while r < 99:
                # 특정한 상황에서 방향을 바꿔주어야 합니다.
                # ladder[r][c]
                # 1. 아래쪽으로 내려오는 경우
                if dir == 0:
                    # 좌,우에 1이있으면 방향전환
                    if c > 0 and ladder[r][c-1] == 1:
                        dir = 1
                    elif c < 99 and ladder[r][c+1]==1:
                        dir = 2
                #2. 좌,우 방향으로 움직일 경우
                    # 아래 방향에 1이있으면 방향전환
                else:
                    #도착지가 1,2인 경우가 있으니 0이 아니면으로 검사
                    if ladder[r+1][c] != 0:
                        dir = 0
                # 현재 방향으로 한 칸씩 이동하기
                r += dr[dir]
                c += dc[dir]

            # r = 99, c = x
            if ladder[r][c] == 2:   # 목적지 찾음
                #i 가 정답
                result = i
                break   #더 이상 출발할 필요 없음

    print(f'#{tc} {result}')