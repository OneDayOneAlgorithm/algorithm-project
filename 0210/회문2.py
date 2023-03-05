import sys
sys.stdin = open('input (5).txt')
for tc in range(1, 11):
    T = int(input())
    board = [input() for _ in range(100)]
    stop = 0
    N = 100
    for M in range(99, 2, -1):  # 회문을 길이 100으로 가정하고 시작
        for i in range(99):      # 행 순회
            for j in range(N - M + 1):  # 열 순회
                # 회문검사 : 회문의 전체 길이의 절반만 검사
                for k in range(M // 2):
                    if board[i][j+k] != board[i][j+M-1-k]:
                        break
                else:
                    print(f'#{tc} {M}')
                    stop = 1
                    break
            if stop == 1:
                break
        if stop == 1:
            break

        for j in range(99):  # 열 순회
            for i in range(N - M + 1):  # 행 순회
                # 회문검사 : 회문의 전체 길이의 절반만 검사
                for k in range(M // 2):
                    if board[i + k][j] != board[i + M - 1 - k][j]:
                        break
                else:
                    print(f'#{tc} {M}')
                    stop = 1
                    break
            if stop == 1:
                break
        if stop == 1:
            break
