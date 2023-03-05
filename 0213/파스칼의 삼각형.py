T = int(input())
for tc in range(1, T + 1):
    N = int(input())                        # N을 4라고 가정한다
    print(f'#{tc}')
    board = [[0] * N for _ in range(N)]     # 정사각형의 0으로 이루어진 보드판을 만든다.
    for i in range(N):                      # 0 1 2 3
        lst = []
        for j in range(i+1):                # 0 1 2 3
            if j == 0:
                board[i][j] = 1             # 0번째 열일 때는 1을 넣는다
            else:
                board[i][j] = board[i-1][j-1] + board[i-1][j]       # 0번째 열이 아닐 때는 위 두수를 더한 값을 넣는
        lst = board[i][:]                   # lst에 board 값을 복사하여 넣고
        while 0 in lst:                     # lst에 있는 0을 모두 삭제한다
            lst.remove(0)
        print(*lst)                         # lst를 언패킹 해서 출력한다
