T = int(input())
for tc in range(T):
    # 이건 임시 리스트
    tmp = []
    # 보드판. 즉 전체 판
    board = []
    # 10번 곱하기 10번해서 100칸짜리 보드판 만듬. 여기 다 0을 집어넣음. 그러면 0이 100개인 보드판 나옴
    for i in range(10):
        for j in range(10):
            tmp.append(0)
        board.append(tmp)
        tmp = []

    N = int(input())
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                # 0인 빈칸에 빨간색이 들어가면 컬러가 1이됨
                # 2인 빈칸에 빨간색이 들어가면 컬러가 3이됨
                # 0인 빈칸에 파란색이 들어가면 컬러가 1이됨
                # 1인 빈칸에 파란색이 들어가면 컬러가 3이됨
                # 즉 3인 컬러의 원소의 갯수가 몇개인지 찾으면됨!!
                if board[j][k] == 0 and color == 1:
                    board[j][k] = 1
                elif board[j][k] == 2 and color == 1:
                    board[j][k] = 3
                if board[j][k] == 0 and color == 2:
                    board[j][k] = 2
                elif board[j][k] == 1 and color == 2:
                    board[j][k] = 3
    cnt = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                cnt += 1
    print(f'#{tc + 1} {cnt}')
