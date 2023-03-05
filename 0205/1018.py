N, M = map(int, input().split())
board = []
lst = []
for _ in range(N):
    word = input()
    board.append(word)
for i in range(N - 7):
    for j in range(M - 7):
        cnt = 0
        cnt2 = 0
        for k in range(i, i+8):
            for t in range(j, j+8):
                if (k + t) % 2:
                    if board[k][t] == 'B':
                        cnt += 1
                    else:
                        cnt2 += 1
                else:
                    if board[k][t] == 'W':
                        cnt += 1
                    else:
                        cnt2 += 1
        lst.append(cnt)
        lst.append(cnt2)
print(min(lst))