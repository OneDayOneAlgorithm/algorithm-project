T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * 10 for _ in range(10)]
    result = 0
    for _ in range(N):
        information = list(map(int,input().split()))
        for i in range(information[0],information[2]+1):
            for j in range(information[1],information[3]+1): 
                if board[i][j] == 0:
                    board[i][j] = information[4]
                elif board[i][j] == 2 and information[4] == 1:
                    board[i][j] = 3
                elif board[i][j] == 1 and information[4] == 2:
                    board[i][j] = 3
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                result += 1
    # print(board)
    print(f'#{tc} {result}')
        

    